data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
sum = 0


# Функция сложения чисел целых и с точкой применяется рекурсия.
def new_sum(*args):
    global sum
    values = args[0]
    # если тип значения int или float - суммируем
    if isinstance(values, int) or isinstance(values, float):
        sum += values
        return
    # если значение список(list), кортеж(tuple) или множество(set) - рекурсия
    elif isinstance(values, list) or isinstance(values, tuple) or isinstance(values, set):
        for i in values:
            new_sum(i)
    # если словарь(dict) - рекурсия только по значению
    elif isinstance(values, dict):
        for key, val in values.items():
            new_sum(val)
    else:
        return


for i in data_structure:
    new_sum(i)

print(sum)
