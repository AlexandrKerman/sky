import datetime

from src import masks


def mask_account_card(user_card: str) -> str:
    """
    Принимает тип и номер карты/счёта в виде str.
    Возвращает Тип карты и замаскированную карту/счёт.
    """
    user_card = str(user_card)
    user_card_number = "".join([i for i in user_card if i.isdigit()])
    user_card_number_length = len(user_card_number)
    if user_card_number_length == 20:
        masked_user_card = masks.get_mask_account(user_card_number)
    elif user_card_number_length == 16:
        masked_user_card = masks.get_mask_card_number(user_card_number)
    else:
        raise ValueError("Invalid card/account number. Expected sequence of 16 or 20 digits.")
    user_card_type = "".join([i for i in user_card if not i.isdigit()]).strip() + " "
    masked_user_card = user_card_type + masked_user_card
    return masked_user_card


def get_date(date: str) -> str:
    """
    Принимает на вход неотформатированную дату в формате
    yyyy-dd-mmThh:mm:ss.ssssss
    """
    parsed_date = datetime.datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%f")
    formatted_date = parsed_date.strftime("%d.%m.%Y")
    return formatted_date
