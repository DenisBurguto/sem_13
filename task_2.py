# Задание No2
# 📌 Создайте функцию аналог get для словаря.
# 📌 Помимо самого словаря функция принимает ключ и
# значение по умолчанию.
# 📌 При обращении к несуществующему ключу функция должна возвращать дефолтное значение.
# 📌 Реализуйте работу через обработку исключений.


def get_from_dict(any_dict: dict, key, value='missed key'):
    try:
        result = any_dict[key]
    except KeyError:
        result = value
    return result


if __name__ == '__main__':
    my_dict = {'ds': 3, (2, 1): 4}
    print(get_from_dict(my_dict, (2,  3)))
    print(get_from_dict(my_dict, 'ds'))
