from src import masks, processing, utils, widget


def main() -> None:
    """
    Точка входа.
    Ничего не принимает, ничего не возвращает
    """

    print(widget.mask_account_card("MasterCard 7158 3007 3472 6758"))
    print(masks.get_mask_account("64686473678894779589"))
    print(widget.get_date("2024-03-11T02:26:18.671407"))
    print(
        processing.sort_by_date(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ]
        )
    )
    operation = utils.get_operations('data/operations.json')[1]
    print(utils.convert_currency_to_rub(operation))


if __name__ == "__main__":
    main()
