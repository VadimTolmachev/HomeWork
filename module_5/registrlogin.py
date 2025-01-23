class Database:
    """
    База данных регистрации пользователей
    """
    def __init__(self):
        self.data = {}

    def add_user(self, username, password):
        self.data[username] = password

class User:
    """
    Класс пользователя содержащий атрибуты: логин, пароль
    """
    def __init__(self, username, password, password_confirm):
        self.username = username
        if password == password_confirm:
            self.password = password

def password_valid(value, len_pwd=8):
    """
    Проверка значения пароля. Длинна не менее 8 символов по умолчанию
    Обязательно заглавная буква и хоть одна цифра.
    """
    if len(value) < len_pwd:
        print('Длинна пароля не соответствует.')
        return False
    upper_case_bl = False
    int_bl = False
    for i in range(len(value)):
        if not int_bl:
            for x in range(10):
                if value[i] == str(x):
                    int_bl = True
        if value[i].isupper():
            upper_case_bl=True
    # print(upper_case_bl, int_bl)
    if upper_case_bl and int_bl:
        return True
    return False

if __name__ == '__main__':
    database = Database()
    while True:
        choice = input('Выберите действие:\n1-Вход\n2-Регистрация\n')

        if choice == '1':
            login = input('Введите логин: ')
            password = input('Введите пароль: ')
            if login in database.data:
                if password == database.data[login]:
                    print('Вход выполнен.')
                    break
                else:
                    print('Неверный пароль. попробуйте еще раз.')
                    continue
            else:
                print('Пользователь не найден.')
                continue

        if choice == '2':
            user = User(input('Введите логин: '), password := input('Введите пароль: '),
                        password2 := input('Подтвердите пароль: '))

            if not password_valid(password):
                print('Пароль не прошел проверку. Попробуйте еще раз.')
                continue
            if password != password2:
                print('Пароли не совпадают. Попробуйте еще раз.')
                continue
            database.add_user(user.username, user.password)
        else:
            print('Действие неопределенно.')
            continue

        print(database.data)
