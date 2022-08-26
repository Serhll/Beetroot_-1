#############################################################################
# LESSONS_13_TASK_#1
"""Write a Python program to detect the number of local variables declared
in a function."""


def count_local_variables():
    a, b, c, d, e, p = 1, 2, 3, 4, 5, 9
    return len(locals())


#############################################################################
# LESSONS_13_TASK_#2
"""Write a Python program to access a function inside a function
(Tips: use function, which returns another function)"""


def outside_function(a, b):
    def inside_function():
        return a ** b

    return inside_function()


#############################################################################
# LESSONS_13_TASK_#3
"""Write a function called `choose_func` which takes a list of nums
and 2 callback functions. If all nums inside the list are positive,
execute the first function on that list and return the result of it.
Otherwise, return the result of the second one"""


def square_nums(nums):
    return [num ** 2 for num in nums]


def remove_negatives(nums):
    return [num for num in nums if num > 0]


def choose_func(nums: list, func1, func2):
    for i in nums:
        if i < 0:
            return func1(nums)
        else:
            return func2(nums)


def main():
    # Task_1
    amount_local_variables = count_local_variables()
    print(amount_local_variables)
    # Task_2
    print(outside_function(500, 2))
    # Task_3
    nums1 = [1, 2, 3, 4, 5]
    nums2 = [1, -2, 3, -4, 5]
    print(choose_func(nums1, square_nums, remove_negatives))
    print(choose_func(nums2, square_nums, remove_negatives))


if __name__ == '__main__':
    main()
