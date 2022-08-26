#############################################################################
# LESSONS_9_TASK_#1
"""A simple function. Create a simple function called favorite_movie, which
takes a string containing the name of your favorite movie. The function should
then print “My favorite movie is named {name}”."""


def favorite_movie(name):
    return f'My favorite movie is named {name}'


#############################################################################
# LESSONS_9_TASK_#2
"""Creating a dictionary.Create a function called make_country, which takes in 
a country’s name and capital as parameters. Then create a dictionary from those 
two, with ‘name’ as a key and ‘capital’ as a parameter. Make the function print 
out the values of the dictionary to make sure that it works as intended."""

country_and_capital_dict = {}


def make_country(country, capital):
    country_and_capital_dict[country] = capital
    return country_and_capital_dict


#############################################################################
# LESSONS_9_TASK_#3
def make_operation(operator, *args):
    if operator == '+':
        addition = sum(args)
        return addition
    if operator == '-':
        minus = args[0]
        for i in args[1:]:
            minus -= i
        return minus
    if operator == '*' and sum(args) > 1:
        multiplication = 1
        for i in args:
            multiplication *= i
        return multiplication
    else:
        return 'Zero'


def main():
    # Task_1
    print(favorite_movie(input('Write your favorite movie:\t')))
    # Task_2
    print(make_country('Ukraine', 'Kyiv'))
    # Task_3
    x = input('Choose and enter arithmetic operator +(+,-,*):')
    print(make_operation(x, 5, 5, -10, -20))


if __name__ == '__main__':
    main()
