import time

def decorator(func):
    """Декоратор, где функция принимает параметры"""
    def wrapper(*args,**kwargs):
        st = time.time()
        res = func(*args,**kwargs)
        et = time.time()
        dt = et-st
        print(f"Время работы {dt} секунд")
        return res
    return wrapper

@decorator
def sum_of_numbers(a,b):
    return a+b

print(sum_of_numbers(2,3))
