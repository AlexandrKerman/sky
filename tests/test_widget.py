import pytest

from src import widget


@pytest.mark.parametrize(
    "number, expected",
    [
        ("MasterCard 7158 3007 3472 6758", "MasterCard 7158 30** **** 6758"),
        ("Visa Gold 5999 414228426353", "Visa Gold 5999 41** **** 6353"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
        ("Счёт 64686473678894779589", "Счёт **9589"),
        ("Счёт 35383033474447895560", "Счёт **5560"),
        ("Счёт 73654108430135874305", "Счёт **4305"),
    ],
)
def test_mask_account_card_valid(number, expected):
    assert widget.mask_account_card(number) == expected


@pytest.mark.parametrize(
    "number", ["dsass2222", "2222222222222222222222222222", "Счёт фыв3 17823678 72638", 3244444442234, 1]
)
def test_mask_account_card_invalid(number):
    with pytest.raises(ValueError):
        widget.mask_account_card(number)


@pytest.mark.parametrize(
    "date, expected", [("2024-03-11T02:26:18.671407", "11.03.2024"), ("2025-02-12T22:26:18.671407", "12.02.2025")]
)
def test_get_date(date, expected):
    assert widget.get_date(date) == expected
