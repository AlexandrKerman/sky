from src import masks


def main() -> None:
    """
    Точка входа.
    Ничего не принимает, ничего не возвращает
    """

    print(masks.get_mask_card_number("7000 7922 8960 6361"))
    print(masks.get_mask_account("73654108430135874305"))


if __name__ == "__main__":
    main()
