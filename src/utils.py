import logging
import redis
from typing import Optional

class RedisConfig:
    def __init__(self, host: str = 'localhost', port: int = 6379, db: int = 0, password: Optional[str] = None):
        self.host = host
        self.port = port
        self.db = db
        self.password = password
        self.redis_client = None

    def connect(self):
        try:
            self.redis_client = redis.Redis(host=self.host, port=self.port, db=self.db, password=self.password)
            self.redis_client.ping()
            logging.info('Connected to Redis')
        except redis.ConnectionError as e:
            logging.error(f'Failed to connect to Redis: {e}')

    def get(self, key: str):
        if self.redis_client:
            return self.redis_client.get(key)
        else:
            logging.error('Redis client is not connected')
            return None

    def set(self, key: str, value: str, expire: int = 0):
        if self.redis_client:
            self.redis_client.set(key, value, ex=expire)
        else:
            logging.error('Redis client is not connected')

    def delete(self, key: str):
        if self.redis_client:
            self.redis_client.delete(key)
        else:
            logging.error('Redis client is not connected')

    def close(self):
        if self.redis_client:
            self.redis_client.close()
            logging.info('Disconnected from Redis')
        else:
            logging.error('Redis client is not connected')

def get_redis_config(host: str = 'localhost', port: int = 6379, db: int = 0, password: Optional[str] = None) -> RedisConfig:
    return RedisConfig(host, port, db, password)