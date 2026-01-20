import pytest

from src import generators


def test_filter_by_currency(dict_list_payments_data):
    generator = generators.filter_by_currency(dict_list_payments_data, "USD")
    assert next(generator) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }
    assert next(generator) == {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    }
    assert next(generator) == {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    }


def test_filter_by_currency_nokey(dict_list_payments_data):
    del dict_list_payments_data[0]["operationAmount"]
    generator = generators.filter_by_currency(dict_list_payments_data, "USD")
    assert next(generator) == {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    }
    assert next(generator) == {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    }


def test_transaction_description(dict_list_payments_data):
    generator = generators.transaction_description(dict_list_payments_data)
    assert next(generator) == "Перевод организации"
    assert next(generator) == "Перевод со счета на счет"
    assert next(generator) == "Перевод со счета на счет"
    assert next(generator) == "Перевод с карты на карту"
    assert next(generator) == "Перевод организации"


@pytest.mark.parametrize(
    "start, stop, excepted_tuple",
    [
        (-1, 2, ("0000 0000 0000 0001", "0000 0000 0000 0002")),
        (1, 3, ("0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003")),
        (9999_9999_9999_9998, 1_0000_0000_0000_0001, ("9999 9999 9999 9998", "9999 9999 9999 9999")),
    ],
)
def test_card_number_generator(start, stop, excepted_tuple):
    generator = generators.card_number_generator(start, stop)
    for i, excepted in enumerate(generator):
        assert excepted == excepted_tuple[i]
