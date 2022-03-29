import sys

from loguru import logger

sys.stdout.reconfigure(encoding="utf-8", errors="backslashreplace")


def configure_logger(level: int) -> Dict[str, Any]:
    """
    Configure the logger.
    """
    n_levels = len(LOG_LEVELS)
    level = n_levels - 1 if level >= n_levels else level
    log_level = LOG_LEVELS[level]
    terminator = "-" * 50
    log_format = (
        """<level>{level}</level> | <green>{time:DD-MM-YY HH:mm:ss}</green> | {name}[{function}():{line}]:\n\n{message}\n"""
        + terminator
    )

    return {
        "handlers": [
            {
                "sink": sys.stdout,
                "format": log_format,
                "colorize": True,
                "level": log_level,
            },
            {
                "sink": "file.log",
                "rotation": "500MB",
                "retention": "10 days",
                "format": log_format,
                "level": log_level,
            },
        ]
    }
