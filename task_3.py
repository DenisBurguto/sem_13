# Задание No3
# 📌 Создайте класс с базовым исключением и дочерние классы- исключения:
# ○ ошибка уровня,
# ○ ошибка доступа.

class MyException(Exception):
    pass


class LevelError(MyException):
    def __init__(self, user_level, needed_level):
        self.user_level = user_level
        self.needed_level = needed_level
        print(f'Your level {self.user_level} is higher than {self.needed_level}')


class AccessError(MyException):
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        print(f'There is no access for user {name} with id {user_id}')


class UserIdError(MyException):

    def __init__(self,user_id):
        self.user_id = user_id
        print(f'User with user_id {self.user_id} is already present')
