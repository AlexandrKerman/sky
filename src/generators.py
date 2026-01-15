def filter_by_currency(dict_list: list[dict], currency: str):
    """
    Принимает list[dict] и currency - тип валюты.
    Возвращает объект генератора,
    выдающий по одному элементу с совпадающей валютой
    """
    if isinstance(dict_list, list):
        for i in dict_list:
            try:
                if i['operationAmount']['currency']['code'] == currency:
                    yield i
            except KeyError:
                continue
    else:
        raise TypeError('Got not a list')


def transaction_description(dict_list: list[dict]):
    if isinstance(dict_list, list):
        for i in dict_list:
            try:
                yield i['description']
            except KeyError:
                yield None
    else:
        raise TypeError('Got not a list')


def card_number_generator(start: int, end: int):
    if start < 1:
        start = 1
    card_generator = ('0' * (16 - len(str(i))) + str(i) for i in range (start, end + 1))
    for i in card_generator:
        if len(i) > 16:
            return
        yield f"{i[:4]} {i[4:8]} {i[8:12]} {i[12:]}"

