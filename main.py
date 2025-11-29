from src import widget


def main() -> None:
    """
    Точка входа.
    Ничего не принимает, ничего не возвращает
    """

    print(widget.mask_account_card("Visa Platinum 7000792289606361"))
    print(widget.get_date("2024-03-11T02:26:18.671407"))


if __name__ == "__main__":
    main()
