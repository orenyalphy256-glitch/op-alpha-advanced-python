# logger_setup.py

# Import necessary modules
import logging
import json
from logging.handlers import RotatingFileHandler

# Name of the log file
LOG_FILE = "logs_batch3.jsonl"
class JsonFormatter(logging.Formatter):
    def format(self, record):
        payload = {"time": self.formatTime(record, "%Y-%m-%dT%H:%M:%SZ"), "level": record.levelname, "msg": record.getMessage()}
        return json.dumps(payload)
    
    def get_logger():
        logger = logging.getLogger("batch3")
        logger.setLevel(logging.INFO)
        handler = RotatingFileHandler(LOG_FILE, maxBytes=2000000, backupCount=3)
        handler.setFormatter(JsonFormatter())
        logger.addHandler(handler)
        return logger