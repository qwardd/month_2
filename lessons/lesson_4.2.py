from time import sleep

def my_decorator(func):
    print(f"Function name: {func.__name__}")
    def wrapper(*args, **kwargs):
        print("До вызова функции")
        func(*args, **kwargs)
        print("После вызова функции")

    return wrapper

@my_decorator
def hello_world():
    print("Hello World!")

@my_decorator
def hello_student():
    print("Hello Student!")

hello_student()

def repeater(n):
    def decorator(func):
        print(f"Function name: {func.__name__}")
        def wrapper(*args, **kwargs):
            print("До вызова функции")
            for i in range(n):
                func(*args, **kwargs)
                sleep(1)
            print("После вызова функции")

        return wrapper

    return decorator


@repeater(3)
def hello_teacher():
    print("Hello Teacher!")

hello_teacher()