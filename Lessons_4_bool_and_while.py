import random
#############################################################################
# LESSONS_3_TASK_#1
"""Write a Python program to get a string made of the first 2 and the last 
2 chars from a given string. If the string length is less than 2, 
return instead of the empty string"""


def two_chars(string_get=input("Please write a random string:\t")):
    if len(string_get) < 2:
        return 'Empty string'
    else:
        return string_get[:2] + string_get[-2:]


print(two_chars())

#############################################################################
# LESSONS_3_TASK_#2
"""The valid phone number program.
Make a program that checks if a string is in the right format for a phone 
number. The program should check that the string contains only numerical 
characters and is only 10 characters long. Print a suitable message depending 
on the outcome of the string evaluation."""

print('~~~The valid phone number program~~~'.upper(), end=' \n\n')


def valid_phone_number(get_number=input('Write a phone number:\t')):
    if get_number.isdigit() and len(get_number) == 10:
        return "Your enter phone number is CORRECT"
    elif get_number.isdigit() and len(get_number) < 10:
        return f'You should write {10 - len(get_number)} more numbers'
    elif len(get_number) > 10:
        return 'Too many numbers'
    else:
        return 'Try again'


print(valid_phone_number())

#############################################################################
# LESSONS_3_TASK_#3
"""The math quiz program. Write a program that asks the answer for a 
mathematical expression, checks whether the user is right or wrong, and then 
responds with a message accordingly."""

number_1 = random.randint(0, 100)
number_2 = random.randint(0, 100)

print(number_1, '+', number_2)
total_result = (number_1 + number_2)
print(total_result)
while True:
    user_enter_total_resalt = input('Write your answer:\t')
    total_result = (number_1 + number_2)
    if not user_enter_total_resalt.isdigit():
        print('Please write a numeric!')
    elif total_result == int(user_enter_total_resalt):
        print('excellent!!'.upper())
        break
    else:
        print('Think again')

#############################################################################
# LESSONS_3_TASK_#4
"""The name check. Write a program that has a variable with your name stored 
(in lowercase) and then asks for your name as input. The program should check 
if your input is equal to the stored name even if the given name has another 
case, e.g., if your input is “Anton” and the stored name is “anton”, 
it should return True."""

my_name = 'Serhii'.lower()
enter_my_name = input('Write your name:\t').lower()
if my_name == enter_my_name:
    print('True')
else:
    print('False')

