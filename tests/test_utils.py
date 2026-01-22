import pytest
from unittest.mock import patch, mock_open

import requests.exceptions

from src import utils


def test_get_operations():
    with patch('builtins.open', mock_open(read_data='[]')):
        assert utils.get_operations('data/test.json') == []


def test_convert_currency_to_rub(capsys):
    with patch('requests.get') as mock_requests:
        mock_requests.return_value.json.return_value = {'result': 200}
        assert utils.convert_currency_to_rub({'operationAmount': {'amount': 100, 'currency': {'code': 'USD'}}}) == 200
        assert utils.convert_currency_to_rub({'operationAmount': {'amount': 200, 'currency': {'code': 'RUB'}}}) == 200
    with patch('requests.get') as mock_requests:
        mock_requests.side_effect = requests.exceptions.ConnectionError
        utils.convert_currency_to_rub({'operationAmount': {'amount': 100, 'currency': {'code': 'USD'}}})
        captured = capsys.readouterr()
        assert captured.out == 'ConnectionError\n'
    with patch('requests.get') as mock_requests:
        mock_requests.side_effect = requests.exceptions.HTTPError
        utils.convert_currency_to_rub({'operationAmount': {'amount': 100, 'currency': {'code': 'USD'}}})
        captured = capsys.readouterr()
        assert captured.out == 'HTTP Error\n'
    with patch('requests.get') as mock_requests:
        mock_requests.side_effect = requests.exceptions.Timeout
        utils.convert_currency_to_rub({'operationAmount': {'amount': 100, 'currency': {'code': 'USD'}}})
        captured = capsys.readouterr()
        assert captured.out == 'Request timed out\n'
    with patch('requests.get') as mock_requests:
        mock_requests.return_value.json.return_value = {'message': 'Looser'}
        utils.convert_currency_to_rub({'operationAmount': {'amount': 100, 'currency': {'code': 'USD'}}})
        captured = capsys.readouterr()
        assert captured.out == 'Plan exceeded. Try later\n'


