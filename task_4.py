# Задание No4
# 📌 Вспоминаем задачу из семинара 8 про сериализацию данных, где в бесконечном цикле запрашивали имя,
# личный идентификатор и уровень доступа (от 1 до 7) сохраняя информацию в JSON файл.
# 📌 Напишите класс пользователя, который хранит эти данные в свойствах экземпляра.
# 📌 Отдельно напишите функцию, которая считывает информацию из JSON файла и формирует множество пользователей.
import json


DEFAULT_LEVEL = '7'


class MyUser:
    """class MyUser create person with name ,ID, authorisation level
    all parameters are strings to be used with json serial
    """

    def __init__(self, name: str, user_id: str, access_level: str = DEFAULT_LEVEL):
        self.name = name
        self.user_id = user_id
        self.access_level = access_level

    def __str__(self):
        return f'User, name: {self.name}, user_id: {self.user_id}, access level: {self.access_level}'

    def __repr__(self):
        return f'MyUser({str(self.name)},{self.user_id},{self.access_level})'

    def __eq__(self, other):
        return self.name == other.name and self.user_id == other.user_id


def create_users_list(file: str = 'user.json'):
    """use json file  filled in following way { access_level:{ user_id:name }} to create users as exemplars of
    MyUser class"""
    try:
        with open(file, 'r', encoding='utf=8') as f:
            data = json.load(f)
            my_users = []
            for item in data:
                for key, value in data[item].items():
                    user_ex = MyUser(value, key, item)
                    my_users.append(user_ex)
    except FileNotFoundError:
        print('Check your file name and try again.')
        my_users = []

    return my_users


if __name__ == '__main__':
    # get_name_id_level('user.json')
    # users = create_users_list()
    # for user in users:
    #     print(user)
    print(help(MyUser))
