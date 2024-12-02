# Крестики - нолики
# Формироуем облясть (area)
import random

area = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]


# Функция проверки по символам
def check_symbol(sm):
    row_bool = [True, True, True]
    count_bool = [True, True, True]
    # Проверка диагоналей
    if area[0][0] == sm and area[1][1] == sm and area[2][2] == sm:
        return True
    if area[2][0] == sm and area[1][1] == sm and area[0][2] == sm:
        return True
    # Проверка строк и столбцов
    for x in range(3):
        for j in range(3):
            if area[j][x] != sm:
                count_bool[x] = False
            if area[x][j] != sm:
                row_bool[x] = False
    if True in row_bool or True in count_bool:
        return True
    return False


# Функция проверки на победителя
def check_winner():
    if check_symbol('X'):
        return 'X'
    if check_symbol('0'):
        return '0'
    return '*'


# Функция бота
def run_bot(symbol=0):
    free_cell = [[], [], []]
    for i in range(len(area)):
        for x in range(len(area[i])):
            if area[i][x] == '*':
                free_cell[i].append(x)
    sim = random.choice(free_cell)
    index_1 = free_cell.index(sim)
    index_2 = random.choice(sim)
    print(f'Бот выбрал строку (1, 2, 3) {index_1 + 1}')
    print(f'Бот выбрал колонку (1, 2, 3) {index_2 + 1}')
    area[index_1][index_2] = symbol

    draw_area(greeting)
    # print(index_1, index_2)


# Функция отрисовки
def draw_area(centre_greeting=''):
    point_ = 0
    if len(centre_greeting) / 2 - 5 > 0:
        point_ = int(len(centre_greeting) / 2 - 5)
    for i in area:
        print(' ' * point_, *i)
    print(' ')


# Запуск игры + Приветствие.
greeting = 'Приветствую вас в игре крестики - нолики'
print(greeting)
print('-' * len(greeting))
draw_area(greeting)
if int(input('Хотите играть с ботом? (1-ДА/0-НЕТ) ')) == 0:
    bot_bool = False
else:
    bot_bool = True

# print(bot_bool)
# Вариант на 9 ходов
for turn in range(1, 10):
    print(f'Ход: {turn}')
    if turn % 2 == 0:
        symbol = '0'
        if bot_bool:
            print('Ходят нолики (БОТ)')
            run_bot()
            continue
        else:
            print('Ходят нолики')
    else:
        if bot_bool:
            print('Ходят креситки (ИГРОК)')
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
