from src import widget, processing


def main() -> None:
    """
    Точка входа.
    Ничего не принимает, ничего не возвращает
    """

    print(widget.mask_account_card("Visa Platinum 7000792289606361"))
    print(widget.get_date("2024-03-11T02:26:18.671407"))
    example_list = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
    print(processing.filter_by_state(example_list))
    print(processing.sort_by_date(example_list))



if __name__ == "__main__":
    main()
