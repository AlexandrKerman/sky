import re


def filter_by_state(dict_list: list[dict], state: str = "EXECUTED") -> list[dict]:
    """
    Принимает на вход список словарей и опциональный ключ (По умолчанию 'EXECUTED').
    Возвращает список словарей, где значение state = опциональному ключу.
    """
    new_dict_list = [i for i in dict_list if i.get("state") == state]
    return new_dict_list


def sort_by_date(dict_list: list[dict], reverse: bool = True) -> list[dict]:
    """
    Принимает на вход список словарей и опциональный ключ порядка сортировки.
    Возвращает новый список словарей, отсортированный по дате (по умолчанию по убыванию)
    """
    new_dict_list = sorted(dict_list, key=lambda x: x.get("date", ""), reverse=reverse)
    return new_dict_list


def process_bank_search(data: list[dict]) -> list[dict]:
    pass


def process_bank_operations(data: list[dict]) -> list[dict]:
    pass
