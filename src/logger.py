# logger.py

import logging

def setup_logger():
    logger = logging.getLogger('CipherToolLogger')
    logger.setLevel(logging.DEBUG)
    file_handler = logging.FileHandler('cipher_tool.log')
    file_handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger

logger = setup_logger()

def log(message, level='info'):
    if level == 'info':
        logger.info(message)
    elif level == 'error':
        logger.error(message)
    elif level == 'warning':
        logger.warning(message)
