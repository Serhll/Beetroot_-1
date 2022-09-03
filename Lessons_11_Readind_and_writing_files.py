import json

# Task_1
"""Write a script that creates a new output file called my_file.txt and writes
the string "Hello file world!" in it. Then write another script that opens
my_file.txt, and reads and prints its contents. Run your two scripts from
the system command line.
Does the new file show up in the directory where you ran your scripts?
What if you add a different directory path to the filename passed to open?
Note: file write methods do not add newline characters to your strings; add
an explicit ‘\n’ at the end of the string if you want to fully terminate the
line in the file."""

with open('Les_10.txt', 'w') as some_text:
    some_text.write('Hello world!')

with open('Les_10.txt') as read_text:
    read_text = read_text.read()

# Task_2
"""Extend Phonebook application
Functionality of Phonebook application:
Add new entries 
Search by first name 
Search by last name 
Search by full name
Search by telephone number
Search by city or state
Delete a record for a given telephone number
Update a record for a given telephone number
An option to exit the program"""

contact_phonebook = {
    'first_name': None,
    # 'last_name': '',
    # 'telephone_number': '',
    # 'city': '',
    # 'state': ''
}


def AddNewPerson():
    contact_phonebook['first_name'] = input('Write name: ').title()
    # last_name = input('Write your last name: ')
    # telephone_number = input('Enter telephone_number: ')
    # city = input('Enter city:')
    # state = input('State: ')

    with open('phonebook.json', 'w') as info:
        json.dump(contact_phonebook, info)

    return contact_phonebook


def search_by_first_name():
    name = input('Write name: ').title()
    if contact_phonebook['first_name'] == name:
        return name
    else:
        return 'It\'s name is not exist in your phonebook'


def search_by_last_name():
    last_name = input('Write name: ').title()
    if contact_phonebook['last_name'] == last_name:
        return last_name
    else:
        return 'It\'s name is not exist in your phonebook'


def main():
    print(contact_phonebook)

    # print(read_text)
    phonebook = AddNewPerson()
    a = phonebook.get('first_name')
    print(a)
    print(contact_phonebook)
    er = search_by_first_name()
    print(er)

if __name__ == '__main__':
    main()
