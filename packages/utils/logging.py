import logging

logging.basicConfig(level=logging.INFO)

def configure_logging(log_level):
    logging.basicConfig(level=getattr(logging, log_level.upper()))
