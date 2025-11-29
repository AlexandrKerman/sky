from src import masks


def mask_account_card(user_card: str) -> str:
    """
    Принимает тип и номер карты/счёта в виде str.
    Возвращает Тип карты и замаскированную карту/счёт.
    """
    user_card_number = ''.join([i for i in user_card if i.isdigit()])
    user_card_number_length = len(user_card_number)
    if user_card_number_length == 20:
        masked_user_card = masks.get_mask_account(user_card_number)
    elif user_card_number_length == 16:
        masked_user_card = masks.get_mask_card_number(user_card_number)
    else:
        raise ValueError('Invalid card/account number. Expected sequence of 16 or 20 digits.')
    user_card_type = user_card[:len(user_card) - user_card_number_length]
    masked_user_card = user_card_type + masked_user_card
    return masked_user_card
