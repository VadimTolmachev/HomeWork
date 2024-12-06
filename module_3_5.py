# Модуль 3 Самостоятельная работа по уроку "Рекурсия"
def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[:1])
    if first == 0:
        first = 1
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first


print(get_multiplied_digits(40203))
print(get_multiplied_digits(402030))

