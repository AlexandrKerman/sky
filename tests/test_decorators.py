import pytest

from src import decorators


def test_log_with_args():
    @decorators.log()
    def my_func(*args, **kwargs):
        return args, kwargs

    expected_return = ((5,), {"var": 5})
    assert my_func(5, var=5) == expected_return


def test_log_logs(capsys):
    @decorators.log()
    def my_func():
        return "successful"

    expected_log = """{\n    "func_name": "my_func",\n    "func_result_valid": "successful",\n\
    "func_exception": null,\n    "args": [],\n    "kwargs": {}\n}\n"""

    result = my_func()
    captured = capsys.readouterr()
    assert captured.out == expected_log
    assert result == "successful"


def test_log_exceptions():
    @decorators.log()
    def my_func():
        raise ValueError

    with pytest.raises(ValueError):
        my_func()
