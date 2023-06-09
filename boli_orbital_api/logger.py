"""
Custom Logger
"""
import logging
import logging.handlers
from logging import config
from pathlib import Path

__all__ = ['setup_logger']


class LevelOnlyFilter:
    def __init__(self, level):
        self.level = level

    def filter(self, record):
        return record.levelno == self.level


logs_dir = Path(__file__).resolve().parent / 'logs'
logs_dir.mkdir(parents=True, exist_ok=True)
LOG_FILE = Path(logs_dir / 'orbitalapi.log')

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "loggers": {
        "root": {
            "level": "INFO",
            "propagate": False,
            # "handlers": ["stream_handler", "rotating_file_handler"],
            "handlers": ["stream_handler"],
        },

        "urllib3": {
            "level": "WARNING",
            "propagate": False,
            # "handlers": ["stream_handler", "rotating_file_handler"],
            "handlers": ["stream_handler"],
        },

    },
    "handlers": {
        "stream_handler": {
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
            "level": "DEBUG",
            "filters": ["only_debug"],
            "formatter": "default_formatter",
        },
        "file_handler": {
            "class": "logging.FileHandler",
            "filename": LOG_FILE,
            "mode": "a",
            "level": "DEBUG",
            "formatter": "file_formatter",
        },
        "rotating_file_handler": {
            "class": "logging.handlers.RotatingFileHandler",
            'maxBytes': 2097152,  # 2Mb
            'backupCount': 5,
            "filename": LOG_FILE,
            "filters": ["only_warning"],
            "mode": "a",
            "level": "DEBUG",
            "formatter": "file_formatter",
        },
    },
    "filters": {
        "only_warning": {
            "()": LevelOnlyFilter,
            "level": logging.WARNING,
        },
        "only_info": {
            "()": LevelOnlyFilter,
            "level": logging.INFO,
        },
        "only_debug": {
            "()": LevelOnlyFilter,
            "level": logging.DEBUG,
        },
    },
    "formatters": {
        "default_formatter": {
            "format": "%(levelname)s - %(name)s - %(funcName)s - %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
        "file_formatter": {
            "format": "%(asctime)s - %(levelname)s - %(name)s - %(funcName)s - %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    },
}


def setup_logger(name: str):
    """
        Setup a logger using defaults
    Args:
        name:

    Returns:

    """

    config.dictConfig(LOGGING_CONFIG)
    logger = logging.getLogger(name)

    return logger
