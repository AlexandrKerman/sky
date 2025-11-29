MASK_SYMBOL = "*"


def get_mask_card_number(card_number: str) -> str:
    """
    Принимает на вход последовательность из 16 цифр в виде строки и возвращает её маску.
    Возвращает замаскированный номер в формате
    XXXX XX** **** XXXX
    """

    card_number = card_number.replace(" ", "")

    for i in card_number:
        if not i.isdigit():
            raise ValueError("Invalid card number. Expected digit sequence")
    if len(card_number) != 16:
        raise ValueError("Invalid card number. Expected 16 digits")

    card_number_list = list(card_number)
    card_number_list = card_number_list[:6] + [MASK_SYMBOL] * 6 + card_number_list[-4:]

    # итерация по списку с конца через каждые 4 элемента
    for i in range(len(card_number_list) - 4, 0, -4):
        card_number_list.insert(i, " ")

    masked_card_number = "".join(card_number_list)

    return masked_card_number


def get_mask_account(account_number: str) -> str:
    """
    Принимает на вход номер счёта из 20 цифр в виде строки и возвращает его маску.
    Номер счёта замаскирвоан и отображается в формате
    **XXXX
    Видны последние 4 цифры номера.
    """

    for i in account_number:
        if not i.isdigit():
            raise ValueError("Invalid account number. Expected digit sequence")
    if len(account_number) != 20:
        raise ValueError("Invalid account number. Expected 20 digits")

    masked_account_number = MASK_SYMBOL * 2 + account_number.replace(" ", "")[-4:]

    return masked_account_number
