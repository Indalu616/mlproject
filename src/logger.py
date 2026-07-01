# logging related code goes here

import logging
import os
from datetime import datetime
import logging
import sys
from src.exception import CustomException
# Create logs directory if it doesn't exist
LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d')}.log"
logs_path= os.path.join(os.getcwd(), "logs",LOG_FILE)

os.makedirs(os.path.dirname(logs_path), exist_ok=True)
# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(lineno)d - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(logs_path),
        logging.StreamHandler()
    ]
)

if __name__ == "__main__": 
    try:
        1/0
    except Exception as e:
        logging.exception("Division by zero error occurred.")
        raise CustomException(e, sys)
    