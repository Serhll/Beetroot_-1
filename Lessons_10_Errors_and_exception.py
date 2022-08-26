#############################################################################
# LESSONS_10_TASK_#1
"""Write a function called oops that explicitly raises an IndexError
exception when called. Then write another function that calls oops inside a
try/except state­ment to catch the error."""


def oops():
    raise IndexError
    # raise KeyError


def oops_2():
    try:
        oops()
    except IndexError:
        print('It\'s Index Error')


#############################################################################
# LESSONS_10_TASK_#2
"""Write a function that takes in two numbers from the user via input(), 
call the numbers a and b, and then returns the value of squared a divided by b, 
construct a try-except block which raises an exception if the two values given 
by the input function were not numbers, and if value b was zero 
(cannot divide by zero). """


def function_(num_1, num_2):
    try:
        print(f'Your result is -->> {(int(num_1) ** 2) / int(num_2)}')
    except ZeroDivisionError:
        print('Сan\'t Division by zero')
    except ValueError:
        print('You must write only number')


def main():
    # Task_1
    oops_2()
    # Task_2
    a = input("Write the first number: ")
    b = input("Write the second number: ")
    function_(a, b)


if __name__ == '__main__':
    main()
