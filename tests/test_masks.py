import pytest

from src import masks


@pytest.mark.parametrize(
    "card, expected",
    [
        ("1596837868705199", "1596 83** **** 5199"),
        ("7158300734726758", "7158 30** **** 6758"),
        ("6831 9824 7673 7658", "6831 98** **** 7658"),
    ],
)
def test_get_mask_card_number_valid(card, expected):
    assert masks.get_mask_card_number(card) == expected


@pytest.mark.parametrize("card", ["1235asdj23", "111111112333333333333333333344444444", None, 1234551])
def test_get_mask_card_number_invalid(card):
    with pytest.raises(ValueError):
        masks.get_mask_card_number(card)


@pytest.mark.parametrize(
    "account, expected",
    [
        ("64686473678894779589", "**9589"),
        ("35383033474447895560", "**5560"),
        ("73654108430135874305", "**4305"),
    ],
)
def test_get_mask_account_valid(account, expected):
    assert masks.get_mask_account(account) == expected


@pytest.mark.parametrize("account", ["12444144444444444134444444123213333", "33312asd2", "sd", 1234, None, []])
def test_get_mask_account_invalid(account):
    with pytest.raises(ValueError):
        masks.get_mask_account(account)
