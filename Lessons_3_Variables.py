first_name = input('What is your name?\t ')
last_name = input('What is your last name?\t')
current_day = input('What is the day in today? ')

#############################################################################
# LESSONS_3_TASK_#1
"""Make a program that has your name and the current day of the week stored
as separate variables and then prints a message"""
print('#'*50)
print('Task_1')
print(f'Good day'
      f' {first_name.upper()}! {current_day.title()} '
      f'is a perfect day to learn python.')

#############################################################################
# LESSONS_3_TASK_#2
"""Save your first and last name as separate variables, then use string 
concatenation to add them together with a white space in between and print 
a greeting."""
print('#'*50)
print('Task_2')
print(f'Hello {first_name.title()} {last_name.title()} !')

#############################################################################
# LESSONS_3_TASK_#3
"""Make a program with 2 numbers saved in separate variables a and b, 
then print the result for each of the following: 

Addition
Subtraction
Division
Multiplication
Exponent (Power)
Modulus
Floor division"""
print('#'*50)
print('Task_3')
print('So let\'s start to do ---->> simple calculator\n'.upper())
print('Simple calculator with two value'.upper())

a = int(input('write the first number:\t'.upper()))
b = int(input('write the second number:\t'.upper()))

action = input('Please choose the action:'
               ' ' + '+, ' '-, ' + '/, ' + '*, ' + '%, ' + '//:\t')


def calculator_action():
    if action == '+':
        return a + b
    elif action == '-':
        return a - b
    elif action == '/':
        return a / b
    elif action == '*':
        return a * b
    elif action == '%':
        return a % b
    elif action == '//':
        return a // b
    else:
        return 'Please choose the action: '


print(calculator_action())
