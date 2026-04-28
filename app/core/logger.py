import logging
import os
from logging.handlers import RotatingFileHandler

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "app.log")
os.makedirs(LOG_DIR, exist_ok=True)


logger = logging.getLogger("job-finder")
logger.setLevel(logging.INFO)

# format
formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

# file handler
file_handler = RotatingFileHandler(
    LOG_FILE,
    maxBytes=5*1024*1024,  # 5 MB
    backupCount=10
)
file_handler.setFormatter(formatter)

# console handler
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

# attach handlers
logger.addHandler(file_handler)
logger.addHandler(console_handler)