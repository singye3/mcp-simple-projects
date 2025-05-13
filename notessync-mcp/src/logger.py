import logging
from logging_json import JSONFormatter

def setup_logger():
    logger = logging.getLogger("notessync_mcp")
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    formatter = JSONFormatter()
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger