#Крестики - нолики
#Формироуем облясть (area)
from ctypes import c_bool

area = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]

# Функция проверки
def check_symbol(sm):
    x_row_bool_1 = True
    x_row_bool_2 = True
    x_row_bool_3 = True
    x_count_bool_1 = True
    x_count_bool_2 = True
    x_count_bool_3 = True
    for x in range(3):
        if area[0][x] != sm:
            x_row_bool_1 = False
        if area[1][x] != sm:
            x_row_bool_2 = False
        if area[2][x] != sm:
            x_row_bool_3 = False
        if area[x][0] != sm:
            x_count_bool_1 = False
        if area[x][1] != sm:
            x_count_bool_2 = False
        if area[x][1] != sm:
            x_count_bool_3 = False
    if x_row_bool_1 or x_row_bool_2 or x_row_bool_3 or x_count_bool_1 or x_count_bool_2 or x_count_bool_3:
        return True
    return False


def check_winner():
    if check_symbol('X'):
        return 'X'
    elif check_symbol('0'):
        return '0'
    return '*'


# Функция отрисовки
def draw_area(centre_greeting=''):
    point_ = 0
    if len(centre_greeting) / 2 - 5 > 0:
        point_ = int(len(centre_greeting) / 2 - 5)
    for i in area:
        print(' ' * point_,*i)
    print(' ')


greeting = 'Приветствую вас в игре крестики - нолики'
print(greeting)
print('-' * len(greeting))
draw_area(greeting)

for turn in range(1,10):
    print(f'Ход: {turn}')
    if turn % 2 == 0:
        print('Ходят нолики')
        symbol = '0'
    else:
        print('Ходят креситки')
        symbol = 'X'
    row = int(input('Введите номер строки (1, 2, 3):')) - 1
    column = int(input('Введите номер столбца (1, 2, 3): ')) - 1
    if area[row][column] == '*':
        area[row][column] = symbol
    else:
        print('Позиция занята, переход хода.')

    draw_area(greeting)

    if check_winner() == 'X':
        print('Победа КРЕСТИКОВ')
        break
    if check_winner() == '0':
        print('Победа НОЛИКОВ')
        break
    if turn == 9:
        print('Ничья.')
