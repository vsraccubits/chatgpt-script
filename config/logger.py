import os
import sys

from loguru import logger

from config import settings

# Path to the error log file
logger_dir = os.path.join(settings.BASE_DIR, "error.log")

# Remove the default console output
logger.remove()

# Add logger for info and error
logger.add(sys.stdout, format="{message}", level="INFO")
logger.add(logger_dir, format="{time} {level} {message}", level="ERROR")
