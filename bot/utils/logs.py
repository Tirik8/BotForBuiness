import logging
import datetime


def start_logging():
    logging.getLogger("sqlalchemy").setLevel(logging.INFO)

    c_handler = logging.StreamHandler()
    c_handler.setLevel(logging.INFO)
    c_handler.setFormatter(
        logging.Formatter("%(asctime)s - %(levelname)s - %(name)s - %(message)s")
    )

    f_handler = logging.FileHandler(f"logs/log-{datetime.date.today()}.log", mode="a")
    f_handler.setLevel(logging.INFO)
    f_handler.setFormatter(
        logging.Formatter("%(asctime)s - %(levelname)s - %(name)s - %(message)s")
    )

    logging.basicConfig(handlers=[c_handler, f_handler], level=logging.INFO)

def log(message):
    logging.info(message)
