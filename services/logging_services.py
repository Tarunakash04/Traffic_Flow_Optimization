import logging
import config

def setup_logging():
    logging.basicConfig(
        filename=config.LOG_FILE,
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    logging.info("Logging initialized")
