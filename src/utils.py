import json
import logging
import os

import pandas as pd
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

#
# logging.basicConfig(level=logging.DEBUG,
#                     format='%(asctime)s | %(name)s | %(levelname)s | %(message)s',
#                     filename='logs/utils.log',
#                     filemode='w')
logger = logging.getLogger("utils_logger")
logger.setLevel(logging.DEBUG)

log_handler = logging.FileHandler("logs/utils.log", mode="w")

formatter = logging.Formatter("%(asctime)s | %(name)s | %(levelname)s | %(message)s")
log_handler.setFormatter(formatter)

logger.addHandler(log_handler)


def get_operations_from_json(path: str) -> list[dict]:
    """
    Получает список словарей из JSON по пути path.
    Возвращает полученный список словарей.
    Если не список -> []
    """
    logger.info(f"Got {path}: {type(path)}")
    logger.info(f"Trying to open file {path}")
    if not path.endswith(".json"):
        logger.warning(f"Got not .json: {path}. Returning empty list...")
        return []
    with open(path, "r", encoding="utf-8") as json_file:
        logger.info("File opened")
        try:
            if isinstance(operations := json.load(json_file), list):
                logger.info("Got valid JSON. Returning...")
                return operations
        except json.JSONDecodeError:
            logger.error("Not valid JSON. Returning empty list...")
            return []
    logger.warning("Something goes wrong. Returning empty list...")
    return []


def get_operations_from_csv(path: str, delimiter: str = ";") -> list[dict]:
    """
    :param path: str - .csv file
    :return: list[dict] of operations in path
    """
    logger.info(f"Got {path}: {type(path)}")
    if not path.endswith(".csv"):
        logger.warning(f"Got not .csv: {path}. Returning empty list...")
        return []
    logger.info("Start reading...")
    df = pd.read_csv(path, delimiter=delimiter)
    logger.info("Reading complete. Returning list of dicts...")
    return df.to_dict("records")


def get_operations_from_excel(path: str) -> list[dict]:
    """
    :param path: str - .xlsx or .xls file
    :return: list[dict] of operations in path
    """
    logger.info(f"Got {path}: {type(path)}")
    if not path.endswith((".xlsx", "xls")):
        logger.warning("Got not excel file (.xslx, .xls). Returning empty list...")
        return []
    logger.info("Start reading...")
    df = pd.read_excel(path)
    logger.info("Reading complete. Returning list of dicts...")
    return df.to_dict("records")


def convert_currency_to_rub(transaction: dict) -> int:
    """
    Получает словарь транзакции.
    Переводит в рубли, если было в иной валюте
    """
    supported_codes = ("USD", "EUR")
    currency_code = transaction.get("operationAmount").get("currency").get("code")
    amount = transaction.get("operationAmount").get("amount")
    logger.info(f"Got transaction with code: {currency_code} and amount: {amount}")
    if currency_code == "RUB":
        logger.info("Code was RUB. No changes, returning amount in RUB...")
        return amount
    if currency_code not in supported_codes:
        logger.critical(f"{currency_code} is not supported code.")
        raise ValueError(f"{currency_code} not in supported codes. Supported codes: {supported_codes}")
    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency_code}&amount={amount}"
    header = {"apikey": API_KEY}
    try:
        logger.info(f"Trying to connect to {url}")
        response = requests.get(url, headers=header, timeout=10).json()
        if "message" in response:
            print("Plan exceeded. Try later")
            logger.error("Plan exceeded. Returning amount without changes")
            return amount
        logger.info(f"Got response. Currency converted with amount {response['result']}")
        return int(response["result"])
    except requests.exceptions.ConnectionError:
        logger.error("ConnectionError")
        print("ConnectionError")
    except requests.exceptions.HTTPError:
        logger.error("HTTP Error")
        print("HTTP Error")
    except requests.exceptions.Timeout:
        logger.error("Request timed out")
        print("Request timed out")
