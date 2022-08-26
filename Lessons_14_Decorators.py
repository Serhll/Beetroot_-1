from functools import wraps
import re

#############################################################################
# LESSONS_14_TASK_#1
"""Task 1
Write a decorator that prints a function with arguments passed to it."""


def logger(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        print(func.__name__, ':arguments is ->>', *args, **kwargs)

    return wrap


@logger
def add(x, y):
    return x + y


@logger
def square_all(*args):
    return [arg ** 2 for arg in args]


#############################################################################
# LESSONS_14_TASK_#2
"""Write a decorator that takes a list of stop words and replaces them
with * inside the decorated function"""


def stop_words(words: list):
    def inner(some_string):
        @wraps(some_string)
        def wrapper(*args, **kwargs):
            replace_string = some_string(*args, **kwargs)
            for word in words:
                replace_string = replace_string.replace(word, '*')
            return replace_string

        return wrapper

    return inner


@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


#############################################################################
# LESSONS_14_TASK_#2

def arg_rules(type_: type, max_length: int, contains: list):
    def inner(function):
        @wraps(function)
        def wrapper(*args):
            for arg in args:
                if not isinstance(arg, type_):
                    print(f'Type of {type_.__name__} is not right')
                    return False
                elif len(arg) > max_length:
                    print(f'Length of {arg} > {max_length}')
                    return False
                check = []
                for i in contains:
                    check.append(re.search(i, arg))
                if not all(check):
                    print('Content is not right')
                    return False
                else:
                    return function(*args)

        return wrapper

    return inner


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


def main():
    # Task_1
    square_all(30, 4)
    add(2, 4)
    # Task_2
    print(create_slogan("Serhii"))
    # Task_3
    assert create_slogan('johndoe05@gmail.com') is False
    assert create_slogan('S@SH05') == \
           'S@SH05 drinks pepsi in his brand new BMW!'
    print(create_slogan('S@SH05'))


if __name__ == '__main__':
    main()
