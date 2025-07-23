from datetime import datetime as dt
from time import sleep

def date(func):
    def wrapper(*args, **kwargs):
        start = dt.now()
        print(f"Функция вызвана в - {start.hour}:{start.minute}:{start.second}   {start.day}/{start.month}/{start.year} ")
        result = func(*args, **kwargs)
        end = dt.now()
        print(f"Функция закончила работу в - {end.hour}:{end.minute}:{end.second}   {end.day}/{end.month}/{end.year} ")
        razn = end - start
        print(f"Функция работала - {razn}")
        return result
        return razn
    return wrapper


@date
def hello_world():
    print("Hello World")
    sleep(5)


hello_world()