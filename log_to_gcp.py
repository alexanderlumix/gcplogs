import logging

# Set up logging configuration
logging.basicConfig(level=logging.ERROR, format='%(levelname)s: %(message)s')

def log_message():
    logger = logging.getLogger(__name__)
    logger.error("This is an ERROR message for GCP logs")

if __name__ == "__main__":
    log_message()