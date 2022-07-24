from constants import MAX_LOGIN_RETRIES, USERNAME, PASSWORD
from helpers import get_input
from getpass import getpass


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password


def get_user_list():
    lines = []
    user_list = []
    with open('database/user.txt') as f:
        lines = f.readlines()

    count = 0
    for line in lines:
        count += 1
        result = [x.strip() for x in line.split(',')]

        if len(result) == 2:
            user_list.append(User(result[0], result[1]))

    return user_list


def is_user_available(username):
    user_list = get_user_list()
    if len(user_list) == 0:
        return None

    limited_list = [element for element in user_list if element.username == username]

    if len(limited_list) == 0:
        return None

    return limited_list[0]


def perform_login():
    number_of_retries = 1
    login_success = False
    user = None
    while number_of_retries <= MAX_LOGIN_RETRIES:

        username = get_input('Your username: ')
        user = is_user_available(username)
        if user is None:
            print("Username not found!")
            continue

        password = getpass('Your password: ')
        number_of_retries += 1

        while user.password != password and number_of_retries <= MAX_LOGIN_RETRIES:
            password = getpass(f'Invalid password. Please retry again {number_of_retries}/{MAX_LOGIN_RETRIES}: ')
            number_of_retries += 1

        if password == PASSWORD:
            login_success = True
            break

    if login_success:
        print('Success')
    else:
        user = None
        print('Failed')

    return user
