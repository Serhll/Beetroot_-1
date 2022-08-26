#############################################################################
# LESSONS_6_TASK_#1
"""The greatest number. Write a Python program to get the largest number from
a list of random numbers with the length of 10"""

import random

random_number_list = []
while user_number := input('Enter your number more 10: \t'):
    while len(random_number_list) < 10 and user_number.isdigit():
        random_number = random.randint(1, int(user_number))
        if random_number not in random_number_list:
            random_number_list.append(random_number)
    if len(random_number_list) == 10:
        print('Random list is:\t' + str(random_number_list).replace('[', '').
              replace(']', ''))
        print('the maximum number is:\t'.title() + str(max(random_number_list)))
        break
    else:
        print('Error, write a number\n'.title())

#############################################################################
# LESSONS_6_TASK_#2
"""Exclusive common numbers. Generate 2 lists with the length of 10 with random 
integers from 1 to 10, and make a third list containing the common integers 
between the 2 initial lists without any duplicates."""

list_1 = []
list_2 = []
numbers_list_1 = input('Enter one number:')
numbers_list_2 = input('Enter one number:')
if numbers_list_1.isdigit() and numbers_list_2.isdigit():
    while len(list_1) < 10:
        a = random.randint(1, int(numbers_list_1))
        if a not in list_1:
            list_1.append(a)
    while len(list_2) < 10:
        a = random.randint(1, int(numbers_list_2))
        if a not in list_2:
            list_2.append(a)
    result = list(set(list_2 + list_1))
    print(list_1)
    print(list_2)
    print(result)
else:
    print('check your input, it must be numbers'.title())

#############################################################################
# LESSONS_6_TASK_#3
""" Extracting numbers. Make a list that contains all integers from 1 to 100,
then find all integers from the list that are divisible by 7 but not a multiple
of 5,and store them in a separate list. Finally, print the list. """
""" LOOP FOR """
list_numbers = [*range(1, 101)]
# print(len(list_numbers))
new_list = []
for i in list_numbers:
    if i % 5 != 0 and i % 7 == 0:
        new_list.append(i)
print(str(new_list).replace('[', '').replace(']', ''))
# print(len(new_list))

"""LOOP WHILE"""
i = 0
new_list = []
while i < 100:
    i += 1
    if i % 5 != 0 and i % 7 == 0:
        new_list.append(i)
print(str(new_list).replace('[', '').replace(']', ''))
