from random import randint

class CorrectUsersData:
    email = 'nastya_andreeva_10@ya.ru'
    password = 'qwerty123'
    username = 'Anastasia'

class RegisteredUserData:
    email = 'registered_user@example.com'
    password = 'password123'
    username = 'RegisteredUser'

class InvalidData:
    email = 'user1@ya.com'
    password = 'passs'
    username = 'Dasha'

class InvalidData_2:
    email = 'user2@ya.com'
    password = 'p'
    username = 'Alexa'


class TestUser:
    def __init__(self):
        self.username = f'alex{randint(0, 999)}'
        self.email = f'privet{randint(0, 999)}@ya.kz'
        self.password = f'pass{randint(0, 999)}hello'

class TestUser2:
    def __init__(self):
        self.username = f'user{randint(0, 9999)}'[:10]  # Имя до 10 символов
        self.email = f'user{randint(0, 999)}@ex.com'[:15]  # Email до 15 символов
        self.password = '123456'  # Пароль длиной 6 символов