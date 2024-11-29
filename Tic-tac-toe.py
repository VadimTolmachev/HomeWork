#Крестики - нолики
#Формироуем облясть (area)
area = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]

# Функция проверки
def check_symbol(sm):
    x_row_bool = [True, True, True]
    x_count_bool = [True, True, True]
    # Проверка диагоналей
    if area[0][0] == sm and area[1][1] == sm and area[2][2] == sm:
        return True
    if area[2][0] == sm and area[1][1] == sm and area[0][2] == sm:
        return True
    # Проверка строк и столбцов
    for x in range(3):
        for j in range(3):
            if area[j][x] != sm:
                x_row_bool[x] = False
            if area[x][j] != sm:
                x_count_bool[x] = False
    if True in x_row_bool or True in x_count_bool:
        return True
    return False


def check_winner():
    if check_symbol('X'):
        return 'X'
    if check_symbol('0'):
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
