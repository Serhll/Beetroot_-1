#############################################################################
# LESSONS_15_TASK_#1
"""A Person class
Make a class called Person. Make the __init__() method take firstname, lastname,
 and age as parameters and add them as attributes. Make another method called
 talk() which makes prints a greeting from the person containing, for example
 like this: “Hello, my name is Carl Johnson, and I’m 26 years old”."""


class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def talk(self):
        print(f'Hello, my name is {self.firstname} {self.lastname} '
              f' and I’m {self.age} years old')


#############################################################################
# LESSONS_15_TASK_#2
"""Doggy age. Create a class Dog with class attribute `age_factor` equals to 7.
Make __init__() which takes values for a dog’s age. Then create a method
`human_age` which returns the dog’s age in human equivalent."""


class Dog:
    age_factor = 7

    def __init__(self, dog_age):
        self.dog_age = dog_age

    def human_age(self):
        return self.dog_age * self.age_factor


#############################################################################
# LESSONS_15_TASK_#3
"""TV controller"""


class TVController:

    def __init__(self, list_channels):
        self.value = None
        self.current_channel = list_channels[0]
        self.list_channels = list_channels

    def first_channel(self):
        self.current_channel = self.list_channels[0]
        return self.current_channel

    def last_channel(self):
        self.current_channel = self.list_channels[-1]
        return self.current_channel

    def turn_channel(self, arg):
        if arg > 3:
            return self.list_channels[0]
        else:
            self.current_channel = self.list_channels[arg - 1]
            return self.current_channel

    def next_channel(self):
        if self.current_channel == self.list_channels[-1]:
            self.current_channel = self.list_channels[0]
            return self.current_channel
        else:
            self.current_channel = self.list_channels[
                self.list_channels.index(self.current_channel) + 1
                ]
            return self.current_channel

    def previous_channel(self):
        if self.current_channel == self.list_channels[0]:
            self.current_channel = self.list_channels[-1]
            return self.current_channel
        else:
            self.current_channel = self.list_channels[
                self.list_channels.index(self.current_channel) - 1
                ]
            return self.current_channel

    def current_channel(self):
        return self.current_channel

    def is_exist(self, value):
        self.value = value
        if self.value in self.list_channels or \
                len(self.list_channels) > value:
            print('Yes')
        else:
            print('No')


def main():
    # Task_1
    person1 = Person('Serhii', 'Bilotserkivets', 30)
    person1.talk()

    # Task_2
    age = Dog(5)
    print(f'Dog age is a {age.dog_age} year\'s and it\'s equivalent'
          f' {age.human_age()} year\'s humans!')

    # Task_3
    CHANNELS = ['BBC', 'Discovery', 'TV1000']
    controller = TVController(CHANNELS)
    print(controller.first_channel())

    print(controller.last_channel())

    print(controller.turn_channel(1))

    print(controller.next_channel())
    print(controller.next_channel())
    print(controller.next_channel())

    print(controller.previous_channel())
    print(controller.previous_channel())

    print(controller.current_channel())

    controller.is_exist(2)
    controller.is_exist("BBC")


if __name__ == '__main__':
    main()
