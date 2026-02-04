from unittest.mock import mock_open, patch

import pandas as pd
import requests.exceptions

from src import utils


def test_get_operations():
    with patch("builtins.open", mock_open(read_data="[]")):
        assert utils.get_operations_from_json("data/test.json") == []


def test_convert_currency_to_rub(capsys):
    with patch("requests.get") as mock_requests:
        mock_requests.return_value.json.return_value = {"result": 200}
        assert utils.convert_currency_to_rub({"operationAmount": {"amount": 100, "currency": {"code": "USD"}}}) == 200
        assert utils.convert_currency_to_rub({"operationAmount": {"amount": 200, "currency": {"code": "RUB"}}}) == 200
    with patch("requests.get") as mock_requests:
        mock_requests.side_effect = requests.exceptions.ConnectionError
        utils.convert_currency_to_rub({"operationAmount": {"amount": 100, "currency": {"code": "USD"}}})
        captured = capsys.readouterr()
        assert captured.out == "ConnectionError\n"
    with patch("requests.get") as mock_requests:
        mock_requests.side_effect = requests.exceptions.HTTPError
        utils.convert_currency_to_rub({"operationAmount": {"amount": 100, "currency": {"code": "USD"}}})
        captured = capsys.readouterr()
        assert captured.out == "HTTP Error\n"
    with patch("requests.get") as mock_requests:
        mock_requests.side_effect = requests.exceptions.Timeout
        utils.convert_currency_to_rub({"operationAmount": {"amount": 100, "currency": {"code": "USD"}}})
        captured = capsys.readouterr()
        assert captured.out == "Request timed out\n"
    with patch("requests.get") as mock_requests:
        mock_requests.return_value.json.return_value = {"message": "Looser"}
        utils.convert_currency_to_rub({"operationAmount": {"amount": 100, "currency": {"code": "USD"}}})
        captured = capsys.readouterr()
        assert captured.out == "Plan exceeded. Try later\n"


def test_get_csv():
    with patch("pandas.read_csv") as mock_csv:
        mock_csv.return_value = pd.DataFrame({"id": [0000, 1111], "amount": [100, 200]})
        assert utils.get_operations_from_csv("data/test.csv") == [
             {"id": 0000, 'state': None, 'date': None, 'operationAmount': {'amount': 100, 'currency': {'name': None, 'code': None}}, 'description': None, 'from': None, 'to': None},
             {"id": 1111, 'state': None, 'date': None, 'operationAmount': {'amount': 200, 'currency': {'name': None, 'code': None}}, 'description': None, 'from': None, 'to': None},
        ]


def test_get_csv_invalid_path():
    with patch("pandas.read_csv") as mock_csv:
        mock_csv.return_value = pd.DataFrame({"id": [0000, 1111], "amount": [100, 200]})
        assert utils.get_operations_from_csv("data/test.txt") == []


def test_get_excel():
    with patch("pandas.read_excel") as mock_excel:
        mock_excel.return_value = pd.DataFrame({"id": [0000, 1111], "amount": [100, 200]})
        assert utils.get_operations_from_excel("data/test.xlsx") == [
            {"id": 0000, 'state': None, 'date': None, 'operationAmount': {'amount': 100, 'currency': {'name': None, 'code': None}}, 'description': None, 'from': None, 'to': None},
            {"id": 1111, 'state': None, 'date': None, 'operationAmount': {'amount': 200, 'currency': {'name': None, 'code': None}}, 'description': None, 'from': None, 'to': None},
        ]


def test_get_excel_xls():
    with patch("pandas.read_excel") as mock_excel:
        mock_excel.return_value = pd.DataFrame({"id": [0000, 1111], "amount": [100, 200]})
        assert utils.get_operations_from_excel("data/test.xls") == [
            {"id": 0000, 'state': None, 'date': None, 'operationAmount': {'amount': 100, 'currency': {'name': None, 'code': None}}, 'description': None, 'from': None, 'to': None},
            {"id": 1111, 'state': None, 'date': None, 'operationAmount': {'amount': 200, 'currency': {'name': None, 'code': None}}, 'description': None, 'from': None, 'to': None},
        ]


def test_get_excel_invalid_path():
    with patch("pandas.read_excel") as mock_excel:
        mock_excel.return_value = pd.DataFrame({"id": [0000, 1111], "amount": [100, 200]})
        assert utils.get_operations_from_excel("data/test.txt") == []
