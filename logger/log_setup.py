# log_setup.py

import logging
import os
from datetime import datetime

def setup_logging(log_level=logging.INFO):
    """
    Sets up a basic logging configuration with a timestamped file and console output.
    """
    LOG_FILE = datetime.now().strftime("log_%Y-%m-%d_%H-%M-%S.log")

    logs_dir = "logs"
    os.makedirs(logs_dir, exist_ok=True)

    LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

    logging.basicConfig(
        filename=LOG_FILE_PATH,
        format="[ %(asctime)s ] %(levelname)s - %(name)s - %(message)s",
        level=log_level,
        filemode='a'
    )

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(logging.Formatter("[ %(asctime)s ] %(levelname)s - %(name)s - %(message)s"))
    logging.getLogger().addHandler(console_handler)