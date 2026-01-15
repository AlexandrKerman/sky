# Виджет банковского приложения

## Описание:
Набор модулей для обработки данных:
- Максировка номера счёта/карты
- Форматирование даты
- Фильтрация операций по статусу
- Сортировка операций по дате

## Установка
1. Клонируйте репозиторий:
```
git clone https://github.com/AlexandrKerman/sky
```
2. Установите зависимости:
```
pip install -r requirements.txt
```

## Использование
Импортируйте необходимые модули из пакета src
```
from src import module_name
```
или
```
import src
```
Или другим удобным способом.

## Пример работы
- get_mask_card_number
```
masked_card = masks.get_mask_card_number('7000792289606361')
# Вернёт '7000 79** **** 6361'
```
- get_masc_account
```
masked_account = masks.get_mask_account('73654108430135874305')
# Вернёт '**4305'
```
- mask_account_card
```
masked_number = widget.mask_account_card('Visa Platinum 7000792289606361')
# Вернёт 'Visa Platinum 7000 79** **** 6361'
```
- get_date
```
formatted_date = widget.get_date('2019-07-03T18:35:29.512364')
# Вернёт 03.07.2019
```
- filter_by_state
```
filtered_list = processing.filter_by_state(list[dict], state='EXECUTED')
# Вернёт список словарей, где ключ 'state' = 'EXECUTED' (по умолчанию)
```
- sort_by_date
```
sorted_by_date = processing.sort_by_date(list[dict], reverse=True)
# Вернёт список словарей, отсортированных по ключу 'date'.
# По умолчанию по убыванию (reverse = True)
```

## Тестирование 
### Отчёт о тестировании последней версии кода сформирован в htmlcov

- Полное тестирование
```
pytest
```
- Покрытие
```
pytest --cov
```
- Экспорт информации о покрытии в формат html
```
pytest --cov=src --covreport=html
```