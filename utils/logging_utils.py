import logging

def setup_logging(log_filename: str):
    """
    Set up logging for the application.

    Args:
        log_filename (str): The path to the log file.
    """
    logging.basicConfig(filename=log_filename, level=logging.INFO, format='%(asctime)s %(message)s')

def log_message(message: str):
    """
    Log a message to the log file.

    Args:
        message (str): The message to log.
    """
    logging.info(message)
