import logging

logger = logging.getLogger("ecommerce_api")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("ecommerce_api.log")
file_handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)
