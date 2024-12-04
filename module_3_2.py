# Проверка адресата
def checking_email(addres):
    variants = ('.ru', '.com', '.net')
    if '@' in addres and addres.lower().endswith(variants):
        return True
    return False


def send_email(message, recipient, *, sender="university.help@gmail.com"):
    if not checking_email(recipient):
        print(f'Невозможно отправить письмо на адрес {recipient}')
    elif not checking_email(sender):
        print(f'Невозможно отправить письмо c адрес {sender}')
    elif recipient == sender:
        print('Нельзя отправить письмо самому себе!')
    elif sender == "university.help@gmail.com":
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')