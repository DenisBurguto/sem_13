# Задание No1
# 📌 Создайте функцию, которая запрашивает числовые данные от пользователя до тех пор, пока он не введёт целое или вещественное число.
# 📌 Обрабатывайте не числовые данные как исключения.

def get_number():
    while True:
        user_input = input("Enter a number: ")
        try:
            num = int(user_input)
            break
        except ValueError:
            try:
                num = float(user_input)
                break
            except ValueError:
                print(f'Please enter  number, please try again.')
    return num



if __name__ == '__main__':
    print(get_number())
