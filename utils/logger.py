"""
===========================================================
File: utils/logger.py

Purpose:
    Configure logging for the entire project.

Author:
    Esa Khan
===========================================================
"""

import logging
from pathlib import Path

from config import LOG_FILE, DEBUG

# Create log directory if it doesn't exist
Path(LOG_FILE).parent.mkdir(parents=True, exist_ok=True)

# Create logger
logger = logging.getLogger("RAG_Resume_System")

# Prevent duplicate logs
if not logger.handlers:

    logger.setLevel(logging.DEBUG if DEBUG else logging.INFO)

    # Log format
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(filename)s | %(message)s"
    )

    # File Handler
    file_handler = logging.FileHandler(LOG_FILE, encoding="utf-8")
    file_handler.setFormatter(formatter)

    # Console Handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # Add Handlers
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)


def log_info(message: str):
    """Log information."""
    logger.info(message)


def log_warning(message: str):
    """Log warning."""
    logger.warning(message)


def log_error(message: str):
    """Log error."""
    logger.error(message)


def log_exception(error: Exception):
    """Log exception with traceback."""
    logger.exception(error)


# ----------------------------------------------------------
# Test Logger
# ----------------------------------------------------------

if __name__ == "__main__":

    log_info("Logger started successfully.")

    log_warning("This is a warning.")

    log_error("This is a sample error.")

    print("\nLogger is working successfully.")
    print(f"Log file location: {LOG_FILE}")