import logging.config
from pathlib import Path


def level_filter_maker(level):
    level = getattr(logging, level)

    def _filter(record):
        return record.levelno <= level

    return _filter


logging_configuration_dict = {
    "version": 1,
    "formatters": {
        "fmt_long": {
            "format": "%(name)s %(asctime)s - %(levelname)-8s - %(filename)-20s - line: %(lineno)d - %(funcName)-20s - %(message)-s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
        "fmt_short": {
            "format": "%(asctime)s - %(levelname)-8s - %(filename)-20s - line: %(lineno)d - %(message)-s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    },
    "filters": {
        "warnings_and_below": {
            "()": "logger.level_filter_maker",
            "level": "WARNING",
        }
    },
    "handlers": {
        "stdout": {
            "class": "logging.StreamHandler",
            "formatter": "fmt_long",
            "level": "DEBUG",
            "stream": "ext://sys.stdout",
            "filters": ["warnings_and_below"],
        },
        "stderr": {
            "class": "logging.StreamHandler",
            "formatter": "fmt_long",
            "level": "ERROR",
            "stream": "ext://sys.stderr",
        },
        "rotating_fh": {
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "fmt_long",
            "filename": Path("LOGFILE.LOG"),
            "mode": "a",
            "maxBytes": 2 * 10 ** 6,
            "backupCount": 9,
            "encoding": "UTF-8",
        },
    },
    "loggers": {
        "main": {
            "level": "DEBUG",
            "propagate": False,
            "handlers": ["stdout", "stderr", "rotating_fh"],
        },
    },
    "root": {
        "level": "DEBUG",
        "handlers": ["stdout", "stderr", "rotating_fh"],
    }
}

logging.config.dictConfig(logging_configuration_dict)
