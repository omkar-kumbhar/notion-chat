import logging
from config.settings import LOG_PATH

def get_logger(name, level=logging.DEBUG, file_level=logging.DEBUG):
    """
    Description:
        Create a logger with the specified name, log level, and file log level.
    Parameters:
        name (str): The name of the logger.
        level (int): The log level for the console handler.
        file_level (int): The log level for the file handler.
    Returns:
        logger (logging.Logger): The logger with the specified name, log level, and file log level.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.propagate = False  # Prevent the log messages from being duplicated in the console

    # Create console handler with a higher log level
    ch = logging.StreamHandler()
    ch.setLevel(level)

    # Create a file handler to write logs to the specified log path
    fh = logging.FileHandler(LOG_PATH)
    fh.setLevel(file_level)

    # Create formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)

    # Add the handlers to the logger
    logger.addHandler(ch)
    logger.addHandler(fh)
    logger.info(f"Logger {name} created.")

    return logger
