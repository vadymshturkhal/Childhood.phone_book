# Python 3.8
# 2020-07-12

"""
Задача
Создайте собственную программу «Адресная книга», работающую из командной строки.
1) Позволяющую:
    + 1. Просматривать,
    + 2. Добавлять,
    + 3. Изменять,
    + 4. Удалять,
    + 5. Искать контактные данные ваших знакомых,
    + 6. Завершать работу программы.

+ 2) Кроме того, эта информация также должна сохраняться на диске для последующего доступа.
"""

import os
import pickle
import warnings

warnings.warn("For execute this program you may have Python version >= 3.8", RuntimeWarning)

NAME = 'textbook.data'
current_directory = os.getcwd()
full_path = current_directory + os.sep + NAME

PHONE_BOOK = {}

COMMANDS = {
    'See': 1,
    'Add': 2,
    'Change': 3,
    'Delete': 4,
    'Search': 5,
    'Exit': 6,
}

if not os.path.exists(full_path):
    print(f'Create a new phone book with name {NAME}.')

    with open(NAME, 'wb') as file:
        pickle.dump(PHONE_BOOK, file)

with open(NAME, 'rb') as file:
    PHONE_BOOK = pickle.load(file)


def show_contacts():
    print('\nYou have this contacts:')
    for k, v in PHONE_BOOK.items():
        print('\t', k, v)
    print('\n')

    return 2


def add_contacts():
    """
    Function adds contact to phone book and rewrites if exist.
    :return: exit code
    """
    while True:
        contact_name = input('Please enter a name of a new contact: ')
        contact_phone = input('Please enter a phone of a new contact: ')

        PHONE_BOOK[contact_name] = contact_phone
        print('Contacts added.\n')

        continue_ = input('If you want to continue enter "Y/y": ')

        if continue_.lower() != 'y':
            break

    return 2


def change_contacts():
    while True:
        contact_name = input('Please enter a name of a contact would you like to change: ')
        contact_phone = input('Please enter a new phone for this contact: ')

        PHONE_BOOK[contact_name] = contact_phone
        print('Contacts changed.\n')

        continue_ = input('If you want to continue enter "Y/y": ')

        if continue_.lower() != 'y':
            break

    return 2


def delete_contacts():
    while True:
        if not PHONE_BOOK:
            print('Sorry, phone book is empty.\n')
            break

        contact_name = input('Please enter a name of a contact would you like to delete: ')
        is_exist = PHONE_BOOK.get(contact_name)
        if is_exist:
            del PHONE_BOOK[contact_name]
            print('User successfully deleted.\n')
        else:
            print('User not found.\n')

        continue_ = input('If you want to continue enter "Y/y": ')

        if continue_.lower() != 'y':
            break

    return 2


def search_contacts():
    while True:
        contact_name = input('Please enter a name of a contact would you like to search: ')

        is_find = PHONE_BOOK.get(contact_name)
        if is_find:
            print(f'\nFound the {contact_name} with number: {PHONE_BOOK[contact_name]}\n')
        else:
            print('\nSorry the contact isn\'t in the phone book.\n')

        continue_ = input('If you want to continue enter "Y/y": ')

        if continue_.lower() != 'y':
            break

    return 2


def verdict_is_correct(validate: str):
    flag = False

    if not validate.isdigit():
        return flag

    if 0 < int(validate) < 7:
        flag = True

    return flag


def what_do_you_want():
    greeting = 'Please make a choice:'
    for_choice = 'I want to:'
    print(greeting, for_choice, sep='\n')

    for k, v in COMMANDS.items():
        print('\t', k, v)

    verdict = input('\nPlease, enter a number with your choice here: ')

    if not verdict_is_correct(verdict):
        print('Sorry, incorrect data. Please try again.\n')
        return 1

    choice = int(verdict)

    return USER_CHOICE[choice]()


USER_CHOICE = {
    1: show_contacts,
    2: add_contacts,
    3: change_contacts,
    4: delete_contacts,
    5: search_contacts,
    6: lambda: 0,
}


def main():
    print('Hello.')
    try:
        while True:
            code = what_do_you_want()
            if code == 0:
                print('\nGoodbye.')
                break
    except KeyboardInterrupt:
        print('\nGoodbye.')
        code = 1
    except EOFError:
        print('\nGoodbye.')
        code = 1
    finally:
        with open(NAME, 'wb') as file:
            pickle.dump(PHONE_BOOK, file)

    return code


exit_code = main()
exit(exit_code)

__version__ = '0.1'
