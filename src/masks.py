import logging

MASK_SYMBOL = "*"


logger = logging.getLogger("masks_logger")
logger.setLevel(logging.DEBUG)

log_handler = logging.FileHandler("logs/masks.log", mode="w")

formatter = logging.Formatter("%(asctime)s | %(name)s | %(levelname)s | %(message)s")
log_handler.setFormatter(formatter)

logger.addHandler(log_handler)


def get_mask_card_number(card_number: str) -> str:
    """
    Принимает на вход последовательность из 16 цифр в виде строки и возвращает её маску.
    Возвращает замаскированный номер в формате
    XXXX XX** **** XXXX
    """
    logger.info(f"Got: {card_number=}:{type(card_number)}")
    card_number = str(card_number).replace(" ", "")

    for i in card_number:
        if not i.isdigit():
            logger.critical("Invalid card number")
            raise ValueError("Invalid card number. Expected digit sequence")
    if len(card_number) != 16:
        logger.critical("Invalid card number.")
        raise ValueError("Invalid card number. Expected 16 digits")

    card_number_list = list(card_number)
    card_number_list = card_number_list[:6] + [MASK_SYMBOL] * 6 + card_number_list[-4:]

    masked_card_number = " ".join(
        ["".join(card_number_list[i - 4 : i]) for i in range(4, len(card_number_list) + 1, 4)]
    )
    logger.info(f"Returned: {masked_card_number}: {type(masked_card_number)}")
    return masked_card_number


def get_mask_account(account_number: str) -> str:
    """
    Принимает на вход номер счёта из 20 цифр в виде строки и возвращает его маску.
    Номер счёта замаскирвоан и отображается в формате
    **XXXX
    Видны последние 4 цифры номера.
    """
    logger.info(f"Got: {account_number=}:{type(account_number)}")
    account_number = str(account_number)
    for i in account_number:
        if not i.isdigit():
            logger.critical("Invalid account number")
            raise ValueError("Invalid account number. Expected digit sequence")
    if len(account_number) != 20:
        logger.critical("Invalid account number")
        raise ValueError("Invalid account number. Expected 20 digits")

    masked_account_number = MASK_SYMBOL * 2 + account_number.replace(" ", "")[-4:]
    logger.info(f"Returned: {masked_account_number}: {type(masked_account_number)}")
    return masked_account_number
