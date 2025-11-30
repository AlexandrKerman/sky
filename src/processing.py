def filter_by_state(dict_list: list[dict], state: str = 'EXECUTED') -> list[dict]:
    """
    Принимает на вход список словарей и опциональный ключ (По умолчанию 'EXECUTED').
    Возвращает список словарей, где значение state = опциональному ключу.
    """
    new_dict_list = [i for i in dict_list if i.get('state') == state]
    return new_dict_list
