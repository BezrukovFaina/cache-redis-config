import logging
import os
import json
from typing import Dict, Any

class Utils:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def load_config(self, file_path: str) -> Dict[str, Any]:
        try:
            with open(file_path, 'r') as file:
                config = json.load(file)
                return config
        except FileNotFoundError:
            self.logger.error(f"Config file not found: {file_path}")
            return {}
        except json.JSONDecodeError as e:
            self.logger.error(f"Failed to parse config file: {e}")
            return {}

    def save_config(self, file_path: str, config: Dict[str, Any]) -> None:
        try:
            with open(file_path, 'w') as file:
                json.dump(config, file, indent=4)
        except Exception as e:
            self.logger.error(f"Failed to save config file: {e}")

    def get_env_var(self, var_name: str) -> str:
        return os.environ.get(var_name)

    def setup_logger(self, log_level: str = 'INFO') -> None:
        logging.basicConfig(level=getattr(logging, log_level.upper()))
        self.logger.info(f"Logger initialized with level: {log_level}")