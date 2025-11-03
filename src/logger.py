import logging
import os
from logging.handlers import RotatingFileHandler

LOG_DIR = os.path.join(os.path.dirname(__file__), "..", "logs")
LOG_FILE = os.path.join(LOG_DIR, "organizer.log")

def setup_logger(log_level=logging.INFO):
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)

    # Create rotating file handler (max 5MB per file, keep 3 backups)
    file_handler = RotatingFileHandler(
        LOG_FILE, maxBytes=5 * 1024 * 1024, backupCount=3, encoding="utf-8"
    )
    file_handler.setLevel(log_level)
    file_handler.setFormatter(logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    ))

    # Optional: Add console output for debugging
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.WARNING)  # Only show warnings/errors in console
    console_handler.setFormatter(logging.Formatter(
        "%(levelname)s - %(message)s"
    ))

    # Apply handlers
    logging.getLogger().handlers.clear()
    logging.getLogger().setLevel(log_level)
    logging.getLogger().addHandler(file_handler)
    logging.getLogger().addHandler(console_handler)
