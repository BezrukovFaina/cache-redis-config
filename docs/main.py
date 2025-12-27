# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0

"""cache-redis-config: A simple cache based on Redis.

This is a basic implementation of a cache system using Redis as the underlying storage.
"""

import os
import redis
from typing import Dict

class Cache:
    """A simple cache using Redis as storage."""
    def __init__(self, host: str = 'localhost', port: int = 6379):
        """Initialize the cache with a Redis connection.

        :param host: The Redis host to connect to.
        :param port: The Redis port to connect to.
        """
        self.conn = redis.Redis(host=host, port=port)

    def store(self, key: str, value: str):
        """Store a value in the cache.

        :param key: The key to store the value under.
        :param value: The value to store.
        """
        self.conn.set(key, value)

    def retrieve(self, key: str) -> str:
        """Retrieve a value from the cache.

        :param key: The key to retrieve the value from.
        :return: The stored value or None if it doesn't exist.
        """
        return self.conn.get(key)

    def delete(self, key: str):
        """Delete a value from the cache.

        :param key: The key to delete the value under.
        """
        self.conn.delete(key)

    def invalidate(self):
        """Flush the cache."""
        self.conn.flushdb()

def main():
    """Main function."""
    if __name__ == '__main__':
        cache = Cache(host='localhost', port=6379)
        cache.store('my_key', 'my_value')
        print(cache.retrieve('my_key'))  # prints: b'my_value'
        cache.delete('my_key')
        print(cache.retrieve('my_key'))  # prints: None
        cache.invalidate()

if __name__ == '__main__':
    main()