import re
from collections import Counter

def filter_by_state(dict_list: list[dict], state: str = "EXECUTED") -> list[dict]:
    """
    Принимает на вход список словарей и опциональный ключ (По умолчанию 'EXECUTED').
    Возвращает список словарей, где значение state = опциональному ключу.
    """
    return [i for i in dict_list if i.get("state") == state]


def sort_by_date(dict_list: list[dict], reverse: bool = True) -> list[dict]:
    """
    Принимает на вход список словарей и опциональный ключ порядка сортировки.
    Возвращает новый список словарей, отсортированный по дате (по умолчанию по убыванию)
    """
    return sorted(dict_list, key=lambda x: x.get("date", ""), reverse=reverse)


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """
    Принимает list[dict] с ключами 'description' и слово для поиска search (str).
    Возвращает list[dict], где было найдено search по ключу 'description'.
    """
    return [i for i in data if re.search(search, str(i.get('description')), flags=re.IGNORECASE)]


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """
    Принимает data: list[dict] и categories: list
    Возвращает dict в виде {'category': count}
    """
    return Counter([description for i in data if (description := i.get('description')) in categories])
