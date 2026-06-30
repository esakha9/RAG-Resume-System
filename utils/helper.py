"""
===========================================================
File: utils/helper.py

Purpose:
    Common helper functions used throughout the project.

Author:
    Esa Khan
===========================================================
"""

import os
import time
from functools import wraps

from config import DEBUG, SHOW_TIME
from utils.logger import logger


# ==========================================================
# Debug Message
# ==========================================================

def debug(message: str):

    if DEBUG:
        print(f"[DEBUG] {message}")

    logger.info(message)


# ==========================================================
# Success Message
# ==========================================================

def success(message: str):

    print(f"[SUCCESS] {message}")

    logger.info(message)


# ==========================================================
# Warning Message
# ==========================================================

def warning(message: str):

    print(f"[WARNING] {message}")

    logger.warning(message)


# ==========================================================
# Error Message
# ==========================================================

def error(message: str):

    print(f"[ERROR] {message}")

    logger.error(message)


# ==========================================================
# Check File Exists
# ==========================================================

def file_exists(file_path: str) -> bool:

    if os.path.exists(file_path):
        return True

    error(f"File not found: {file_path}")
    return False


# ==========================================================
# Timer Decorator
# ==========================================================

def timer(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()

        if SHOW_TIME:
            print(f"[TIME] {func.__name__} : {end-start:.2f} seconds")

        return result

    return wrapper


# ==========================================================
# Print Title
# ==========================================================

def print_title(title: str):

    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


# ==========================================================
# Test Helper Functions
# ==========================================================

if __name__ == "__main__":

    print_title("Helper Test")

    debug("Debug message")

    success("Everything is working.")

    warning("This is only a warning.")

    error("This is a sample error.")

    print(file_exists("config.py"))


    @timer
    def test():

        time.sleep(2)


    test()