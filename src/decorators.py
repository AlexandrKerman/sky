from functools import wraps
from json import dumps


def log(file_name = None):
    """
    Ведёт логи выполнения декорируемой функции.
    По умолчанию в cmd, file - в конкретный файл
    """
    def func_handler(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            log_data = {}
            exception = None
            func_result = None
            try:
                func_result = func(*args, **kwargs)
            except Exception as e:
                exception = str(e)
                raise
            finally:
                log_data = {'func_name': func.__name__,
                            'func_result_valid': func_result, #Дописать
                            'func_exception': exception,
                            'args': args,
                            'kwargs': kwargs}
                log_data_json = dumps(log_data, indent=4, ensure_ascii=False)
                if file_name:
                    with open(file_name, 'a', encoding='utf-8', newline='\n') as file:
                        file.write(f'{log_data_json}\n')
                else:
                    print(log_data_json)
            return func_result
        return wrapper
    return func_handler