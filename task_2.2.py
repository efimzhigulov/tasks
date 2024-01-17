import time
from datetime import datetime
from functools import wraps

def log_function(name_of_log):
    def func_decorator(func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            res = func(*args,**kwargs)
            t = time.time()
            local = datetime.fromtimestamp(t)
            with open(name_of_log,"a") as log:
                create_log = log.write(f'Function: {wrapper.__name__}\n'
                                       f'Arguments: {args}\n'
                                       f'Result: {res}\n'
                                       f'Timestamp: {local}\n\n')
                print(create_log)
            return res
        return wrapper
    return func_decorator


@log_function("log.txt")
def sum_of_numbers(a,b):
    return a+b


print(sum_of_numbers(2,3))