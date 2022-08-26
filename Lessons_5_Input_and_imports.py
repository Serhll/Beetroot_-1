import random

#############################################################################
# LESSONS_3_TASK_#1
"""The Guessing Game. Write a program that generates a random number 
between 1 and 10 and lets the user guess what number was generated.
The result should be sent back to the user via a print statement."""
print('Task_1')
while True:
    number_random_string = random.randint(1, 10)
    your_numbers = int(input('Write your number: '))
    if number_random_string == your_numbers:
        print('Excellent you guessed right')
        break
    elif number_random_string > your_numbers:
        print(
            f' Your number is {your_numbers} less than {number_random_string}')
        continue
    else:
        print(
            f' Your number is {your_numbers} more than {number_random_string}')

#############################################################################
# LESSONS_3_TASK_#2
print('*' * 80)
print('Task_2')
"""The birthday greeting program.
Write a program that takes your name as input, and then your age as input and 
greets you with the following:"""

name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f'Hello {name.upper()}, on your next birthday you’ll '
      f'be {age + 1} years!')

#############################################################################
# LESSONS_3_TASK_#3
print('*' * 80)
print('Task_3')
"""Words combination. Create a program that reads an input string and then 
creates and prints 5 random strings from characters of the input string."""

enter_string = list(input("Write your different word or string: "))
random.shuffle(enter_string)
new_string = ' '.join([str(a) for a in enter_string])
print(new_string.replace(' ', ''))
