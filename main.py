from src import generators, processing, utils, widget


def get_operation_type(skip_hello: bool = False) -> tuple:
    operations_from_file = {
        "1": (
            utils.get_operations_from_json,
            {"path": "data/operations.json", "no_none": True},
            "Для обработки выбран JSON-файл",
        ),
        "2": (
            utils.get_operations_from_csv,
            {"path": "data/transactions.csv", "no_none": True},
            "Для обработки выбран CSV-файл",
        ),
        "3": (
            utils.get_operations_from_excel,
            {"path": "data/transactions_excel.xlsx", "no_none": True},
            "Для обработки выбран XLSX-файл",
        ),
    }

    if not skip_hello:
        print(
            "Привет! Добро пожаловать в программу работы с банковскими транзациями.\n"
            "Выберите необходимый пункт меню:"
        )

    print(
        "1. Получить информацию о транзациях из JSON-файла\n"
        "2. Получить информацию о транзациях из CSV-файла\n"
        "3. Получить информацию о транзакциях из XLSX-файла"
    )
    user_input = input("Ваш ответ: ").strip()

    if valid_answer := operations_from_file.get(user_input):
        return valid_answer
    else:
        print(f"{user_input} нет в меню выбора. Попробуйте снова.\n")
        return get_operation_type(True)


def get_filter():
    valid_filters = ("EXECUTED", "CANCELED", "PENDING")
    print(
        "\nВведите статус, по которому необходимо выполнить фильтрацию.\n" "Доступные для фильтровки статусы:",
        ", ".join(valid_filters),
    )
    if (user_input := input("Ваш ответ: ").strip().upper()) in valid_filters:
        return user_input
    print("Введён некорректный фильтр. Попробуйте снова")
    return get_filter()


def main() -> None:
    read_operation = get_operation_type()
    print(read_operation[2])
    operations_data = read_operation[0](**read_operation[1])
    selected_filter = get_filter()
    filtered_data = processing.filter_by_state(operations_data, selected_filter)
    print(f'Операции отфильтрованы по статусу "{selected_filter}"')

    print("\nОтсортировать операции по дате? Да/Нет")
    while (user_input := input("Ваш ответ: ").strip().lower()) not in ("да", "нет"):
        print("Некорректный ответ. Повторите ещё раз. Да/Нет")
    if user_input == "да":
        print("\nОтсортировать по возрастанию или по убыванию?")
        while not (user_input := input("Ваш ответ: ").strip().lower()).endswith(("возрастанию", "убыванию")):
            print("Некорректный ответ. Повторите ещё раз.\n" "По возрастанию / По убыванию")
        if user_input.endswith("возрастанию"):
            filtered_data = processing.sort_by_date(filtered_data, reverse=False)
            print("Отфильтровано по возрастанию.\n")
        else:
            filtered_data = processing.sort_by_date(filtered_data)
            print("Отфильтровано по убыванию\n")

    print("\nВыводить только рублёвые транзакции? Да/Нет")
    while (user_input := input("Ваш ответ: ").strip().lower()) not in ("да", "нет"):
        print("Некорректный ответ. Повторите ещё раз. Да/Нет")
    if user_input == "да":
        filtered_data = [i for i in generators.filter_by_currency(filtered_data, "RUB")]
        print("Данные отфильтрованы по рублёвым")

    print("\nОтфильтровать список транзаций по определённому слову в описании? Да/Нет")
    while (user_input := input("Ваш ответ: ")).strip().lower() not in ("да", "нет"):
        print("Некорректный ответ. Повторите ещё раз. Да/Нет")
    if user_input == "да":
        print("\nПо какому слову отфильтровать?")
        user_input = input("Ваш ответ: ").strip()
        filtered_data = processing.process_bank_search(filtered_data, user_input)
        print(f'Список транзакций отфильтрован по наличию слова "{user_input}".')

    data_len = len(filtered_data)
    print(
        "\nРаспечатываю итоговый список транзакций...\n" f"Всего банковских операций в выборке: {len(filtered_data)}"
    )
    if data_len:
        print(
            *[
                f"{widget.get_date(i.get('date'))} {i.get('description')}\n"
                f"{f'{widget.mask_account_card(i.get('from'))} -> ' if widget.mask_account_card(i.get('from')) else ''}{widget.mask_account_card(i.get('to'))}\n"
                f"{i['operationAmount']['amount']} {i['operationAmount']['currency']['name']}"
                for i in filtered_data
            ],
            sep="\n\n",
        )
    else:
        print("\nНе найдено ни одной транзации, подходящей под ваши условия фильтрации.")


if __name__ == "__main__":
    main()
