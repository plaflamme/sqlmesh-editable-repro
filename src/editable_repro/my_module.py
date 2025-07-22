import logging

logger = logging.getLogger(__name__)


def my_function() -> str:
    logger.info("This is a log message from my_function.")
    return "Hello, World!"
