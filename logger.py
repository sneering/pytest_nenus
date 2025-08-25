from loguru import logger
import sys
from datetime import datetime

# Remove default logger
logger.remove()

# Console logs only INFO and above
logger.add(
    sys.stderr,
    level="INFO",
    colorize=True,
    enqueue=True,
    backtrace=True,
    diagnose=True,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
           "<level>{level: <8}</level> | "
           "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - "
           "<level>{message}</level>",
)

# File logs everything (DEBUG and above)
log_filename = f"logs/test_run_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
logger.add(
    log_filename,
    level="DEBUG",
    # rotation="1 day",      # create a new file each day
    # retention="7 days",    # keep logs for 7 days
    compression="zip",     # old logs compressed
    enqueue=True,
    backtrace=True,
    diagnose=True,
    format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function}:{line} - {message}",
)

__all__ = ["logger"]