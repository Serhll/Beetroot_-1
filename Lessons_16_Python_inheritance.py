# from pprint import pprint

#############################################################################
# LESSONS_16_TASK_#1
"""Make a class structure in python representing people at school.
Make a base class called Person, a class called Student, and another one
called Teacher. Try to find as many methods and attributes as you can which
belong to different classes, and keep in mind which are common and which are
not. For example, the name should be a Person attribute, while salary should
only be available to the teacher. """


class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


class Teacher(Person):
    def __init__(self, name, age, subject: str, teaching_hours=20):
        super().__init__(name, age)
        self.subject = subject
        self.teaching_hours = teaching_hours
        self.pay_per_hours = 15
        self.value_award = 10
        self.total_salary = 0

    def count_salary_per_week(self):
        if self.teaching_hours < 40:
            self.total_salary += self.pay_per_hours * self.teaching_hours
            return self.total_salary
        else:
            self.total_salary += (self.pay_per_hours * self.teaching_hours
                                  * (1 + (self.value_award / 100)))
            return f'Total salary per week {self.total_salary} USD.\n'


class Student(Person):
    def __init__(self, name, age, type_of_education='offline'):
        super().__init__(name, age)
        self.type_of_education = type_of_education

    def get_type_education(self):
        if self.type_of_education == 'offline':
            return f'You have {self.type_of_education}  ' \
                   f'education. Look board with schedule'
        else:
            return f'You have {self.type_of_education} education. ' \
                   f'Get the link and watch the lecture!'


#############################################################################
# LESSONS_16_TASK_#2
"""Mathematician. Implement a class Mathematician which
is a helper class for doing math operations on lists"""


class Mathematician:
    @staticmethod
    def square_nums(lst):
        square_lst = [i ** 2 for i in lst]
        print(f'Squares of numbers list: {square_lst}')
        return square_lst

    @staticmethod
    def remove_positives(lst):
        negative_lst = [i for i in lst if i < 0]
        print(f'List of negative numbers: {negative_lst}')
        return negative_lst

    @staticmethod
    def filter_leaps(lst):
        leap_years_lst = [i for i in lst if i % 4 == 0]
        print(f'Leap years list: {leap_years_lst}')
        return leap_years_lst


#############################################################################
# LESSONS_16_TASK_#3
"""Product Store"""


class Product:
    def __init__(self, type_: str, name: str, price: int):
        self.product_type = type_
        self.product_name = name
        self.product_price = price

        print(self.product_name, self.product_type, self.product_price)


class ProductStore:
    def __init__(self):
        self.warehouse = []
        self.margin = 1.3
        self.product = None
        self.income = 0

    def add(self, product: Product, amount):
        pass


#############################################################################
# LESSONS_16_TASK_#4
"""Custom exception. Create your custom exception named `CustomException`, 
you can inherit from base Exception class, but extend its functionality to 
log every error message to a file named `logs.txt`. Tips: Use __init__ 
method to extend functionality for saving messages to file"""


class CustomException(Exception):
    def __init__(self, msg):
        with open('Lessons_16_Task_4_log.txt', 'a') as file:
            file.write(msg + '\n')


def main():
    # Task_1
    teachers_math = Teacher('Serhii', 30, 'Mathematics', 41)
    print(teachers_math.count_salary_per_week())
    student_1 = Student('Serhii', 18, 'online')
    print(student_1.get_type_education())

    # Task_2
    m = Mathematician()
    assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]
    assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]
    assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]

    # Task_3
    lst_things_1 = Product('T-short', 'Nike', 50)
    lst_things_2 = Product('Sneakers', 'Adidas', 350)
    lst_things_1.product_type()

    # Task_4
    raise CustomException('Message')


if __name__ == '__main__':
    main()
