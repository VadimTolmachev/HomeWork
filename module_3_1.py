calls = 0


def count_calls():
    global calls
    calls += 1
    return 0


def string_info(string):
    count_calls()
    return string.__len__(), string.upper(), string.lower()


def is_contains(string, list_to_search):
    count_calls()
    for i in range(len(list_to_search)):
        if string.upper() == list_to_search[i].upper():
            return True
    return False


print(string_info('Histori'))
print(string_info('Ambbar'))
print(is_contains('Поиск', ['Строка', 'Список', 'поиск']))
print(is_contains('corvet',['galeon', 'CARAVELLA']))
print(calls)
