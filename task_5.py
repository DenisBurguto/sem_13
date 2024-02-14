# Задание No5
# 📌 Доработаем задачи 3 и 4. Создайте класс проекта, который имеет следующие методы:
# 📌 загрузка данных (функция из задания 4)
# 📌 вход в систему - требует указать имя и id пользователя. Для проверки наличия пользователя в множестве
# используйте магический метод проверки на равенство пользователей. Если такого пользователя нет, вызывайте
# исключение доступа. А если пользователь есть, получите его уровень из множества пользователей.
# 📌 добавление пользователя. Если уровень пользователя меньше, чем ваш уровень, вызывайте исключение уровня доступа.
import json
from sem_13.task_4 import create_users_list, MyUser
from sem_13.task_3 import AccessError, LevelError, UserIdError


class MyProject:
    """class works with json file to read and write users authorisation data
    can check permissions of user, can add new users

    """

    def __init__(self, json_file: str = 'user.json'):
        self.users = create_users_list(json_file)
        self.access_level = 0
        self.system_access = False
        print(f"current system status is {'activated' if self.system_access else 'deactivated'}")
        print(f'current users list containing {len(self.users)} users.')

    def enter_to_system(self, name, user_id):
        match = False
        log_user = MyUser(name, user_id)
        if not self.users:
            log_user.access_level = self.access_level
            self.add_user(log_user)
            self.system_access = True
            print(f"current system status is activated by  {log_user}")
            return MyUser(name, user_id).access_level
        for user in self.users:
            if user == log_user:
                match = True
                self.access_level = user.access_level
        if not match:
            raise AccessError(name, user_id)
        self.system_access = True
        print(f"current system status is activated by  {log_user}")
        return self.access_level

    def add_user(self, user: MyUser):
        if int(user.access_level) < int(self.access_level):
            raise LevelError(self.access_level, user.access_level)
        for authorized in self.users:
            if authorized.user_id == user.user_id:
                raise UserIdError(user.user_id)
        self.users.append(user)
        self.from_users_list_to_json()

    def from_users_list_to_json(self, json_file: str = 'user.json'):
        out_dict = {}
        for user in self.users:
            if not out_dict.get(user.access_level):
                pairs = {user.user_id: user.name}
                out_dict[user.access_level] = pairs
            else:
                out_dict.get(user.access_level)[user.user_id] = user.name
        with open(json_file, 'w', encoding='utf-8') as out:
            json.dump(out_dict, out, indent=2)


if __name__ == '__main__':
    new = MyProject()
    new.enter_to_system('den', '0',)
    print(new.access_level)
    test_user_4 = MyUser('test4', '9', '3')
    new.add_user(test_user_4)
    test_user = MyUser('test', '8')


    new.add_user(test_user)
    new.enter_to_system('test', '8')
    print(new.access_level)

    # new.add_user(MyUser('df5', '17', '7'))
