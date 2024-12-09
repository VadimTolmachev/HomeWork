# Максимум в списке
# Подсчёт четных чисел в списке
# Уникальный список


def find_max(list_):
    max_ = list_[0]
    for i in list_:
        if i > max_:
            max_ = i
    return max_


# print(find_max([1, 2, 1, 5, 0]))


def count_even(list_):
    counter = 0
    for i in list_:
        if i == 0:
            continue
        if i % 2 == 0:
            counter += 1
    return counter


# print(count_even([2, 2, 3, 4, 2, 1, 0]))

def unique(list_):
    new_list = []
    for i in list_:
        if i not in new_list:
            new_list.append(i)

    return new_list


print(unique([1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8]))
