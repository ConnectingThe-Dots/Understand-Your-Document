import logging

def setup_logger(level="INFO"):
    lvl = getattr(logging, level.upper(), logging.INFO)
    logging.basicConfig(format="%(asctime)s %(levelname)s: %(message)s", level=lvl)
