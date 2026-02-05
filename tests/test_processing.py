from src import processing


def test_filter_by_state(dict_list_raw_data):
    assert processing.filter_by_state(dict_list_raw_data) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
    assert processing.filter_by_state(dict_list_raw_data, "CANCELED") == [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


def test_filter_by_state_invalid():
    assert processing.filter_by_state([]) == []


def test_sort_by_date(dict_list_raw_data):
    assert processing.sort_by_date(dict_list_raw_data) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_sort_by_date_invalid():
    assert processing.sort_by_date([]) == []


def test_bank_search():
    data = [
        {"description": "some_Description"},
        {"description": "some_another_description"},
        {"description": "no"},
        {},
    ]
    result = processing.process_bank_search(data, search="description")
    assert result == [{"description": "some_Description"}, {"description": "some_another_description"}]


def rest_bank_operations():
    data = [
        {"description": "some_Description"},
        {"description": "some_another_description"},
        {"description": "no"},
        {"description": "no"},
        {},
    ]
    result = processing.process_bank_operations(data, categories=["some_Description", "no"])
    assert result == {"some_Description": 1, "no": 2}
