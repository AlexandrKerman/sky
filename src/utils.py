import json
import os

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")


def get_operations(path: str) -> list[dict]:
    """
    Получает список словарей из JSON по пути path.
    Возвращает полученный список словарей.
    Если не список -> []
    """
    with open(path, "r", encoding="utf-8") as json_file:
        try:
            if isinstance(operations := json.load(json_file), list):
                return operations
        except json.JSONDecodeError:
            return []
    return []


def convert_currency_to_rub(transaction: dict) -> int:
    """
    Получает словарь транзакции.
    Переводит в рубли, если было в иной валюте
    """
    supported_codes = ("USD", "EUR")
    currency_code = transaction.get("operationAmount").get("currency").get("code")
    amount = transaction.get("operationAmount").get("amount")
    if currency_code == "RUB":
        return amount
    if currency_code not in supported_codes:
        raise ValueError(f"{currency_code} not in supported codes. Supported codes: {supported_codes}")
    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency_code}&amount={amount}"
    header = {"apikey": API_KEY}
    try:
        response = requests.get(url, headers=header, timeout=10).json()
        if "message" in response:
            print("Plan exceeded. Try later")
            return amount
        return int(response["result"])
    except requests.exceptions.ConnectionError:
        print("ConnectionError")
    except requests.exceptions.HTTPError:
        print("HTTP Error")
    except requests.exceptions.Timeout:
        print("Request timed out")
