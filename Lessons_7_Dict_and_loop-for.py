#############################################################################
# LESSONS_7_TASK_#1
"""Make a program that has some sentence (a string) on input and returns a dict
containing all unique words as key sand the number of occurrences as values."""
import pprint

sentence = \
    'In school we learn that mistakes are bad, and we are punished for ' \
    'making them.  Yet, if you look at the way humans are designed to learn,' \
    ' we learn by making mistakes. We learn to walk by falling down. If we ' \
    'never fell down, we would never ' \
    'walk.'.lower().replace(',', '').replace('.', '')
# Write our sentence to list
word_list_from_sentence = list(sentence.split(' '))
print(word_list_from_sentence)
# Convert our list to set
convert_to_set = set(word_list_from_sentence)
# Create a dictionary containing all unique words as keys and the number
# of occurrences as values.
d2ct = {j: word_list_from_sentence.count(j)
        for i in range(len(word_list_from_sentence)) for j in convert_to_set
        }
# Classic record loop 'for':
# for i in range(len(word_list_from_sentence)):
#     for j in convert_to_set:
#         d2ct[j] = word_list_from_sentence.count(j)
pprint.pprint(d2ct)

#############################################################################
# LESSONS_7_TASK_#2
"""Task 2
Create a function which takes as input two dicts with structure mentioned above,
then computes and returns the total price of stock."""
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}


# print(f'Food count: {stock}'.replace('{', '').replace('}', ''), end='\n'*2)
# print(f'Food prices: {prices}'.replace('{', '').replace('}', ''), end='\n'*2)


def total_cost():
    # Check length of dictionaries
    if len(stock) != len(prices):
        return f'The number of keys in dictionaries is different stock:' \
               f' {len(stock)} and price: {len(prices)}'
    # Check the name of keys in dictionaries
    elif list(stock.keys()) != list(prices.keys()):
        a, b = set(stock.keys()), set(prices.keys())
        return (
            f'Something was wrong! The keys in the dictionary are difference: '
            f'{a.symmetric_difference(b)}'.replace('{', '').replace('}', ''))
    # Count total price
    else:
        lst = [prices[x] * stock[x] for x in stock]
        return f'Total price of food is: {sum(lst)} UAH'


print(total_cost())

#############################################################################
# LESSONS_7_TASK_#3
"""List comprehension exercise. Use a list comprehension to make a list 
containing tuples (i, j) where `i` goes from 1 to 10 and `j` is corresponding 
to `i` squared."""


# Example_1
def l1st_with_tuples_1():
    lst_of_tuples_1 = []
    lst = []
    for i in range(1, 11):
        lst.append(i)
        lst_of_tuples_1 = []
        for index, item in enumerate(lst):
            lst_of_tuples_1.append((item, item * item))
    return lst_of_tuples_1


print(l1st_with_tuples_1())


# Example_2
def l1st_with_tuples_2():
    lst_of_tuples_2 = [(item, item ** 2) for value, item in
                       enumerate(range(1, 11))]
    return lst_of_tuples_2


print(l1st_with_tuples_2())
