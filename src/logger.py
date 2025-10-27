# Week 5: Logging and error handling
# Step 1: Create a logging setup
import logging
import os

LOG_DIR = os.path.join(os.path.dirname(__file__), "..", "logs")
LOG_FILE = os.path.join(LOG_DIR, "organizer.log")

def setup_logger():
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)

    logging.basicConfig(
        filename=LOG_FILE,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )