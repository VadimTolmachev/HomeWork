# Максимум в списке
# Подсчёт четных чисел в списке
# Уникальный список


def find_max(list_):
    max_ = list_[0]
    for i in list_:
        if i > max_:
            max_ = i
    return max_


def find_min(list_):
    min_ = list_[0]
    for i in list_:
        if min_ > i:
            min_ = i

    return min_


print(find_min([3, 5, 67, 0, -2, 45]))


# print(find_max([1, 2, 1, 5, 0]))


def count_even(list_):
    counter = 0
    for i in list_:
        if i == 0:
            continue
        if i % 2 == 0:
            counter += 1
    return counter


def count_odd(list_):
    counter = 0
    for i in list_:
        if i % 2 != 0:
            counter += 1
    return counter


# print(f'Количество нечетных значений списка - {count_odd([3,5,7,2,4,8,13,11,14])}')
# print(count_even([2, 2, 3, 4, 2, 1, 0]))

def unique(list_):
    new_list = []
    for i in list_:
        if i not in new_list:
            new_list.append(i)

    return new_list


print(unique([1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8]))
