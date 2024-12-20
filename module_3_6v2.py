data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
sum_ = 0
len_str = 0


# Функция сложения чисел и длинны строк.
def new_sum(*args):
    global sum_, len_str
    values = args[0]
    # если тип значения int или float - суммируем
    if isinstance(values, int) or isinstance(values, float):
        sum_ += values
        return
    # если значение список(list), кортеж(tuple) или множество(set) - рекурсия
    elif isinstance(values, list) or isinstance(values, tuple) or isinstance(values, set):
        if isinstance(values, list):
            print(f'длинна списка - {len(values)} - {values}')
        elif isinstance(values, tuple):
            print(f'длинна кортэжа - {len(values)} - {values}')
        else:
            print(f'длинна множества - {len(values)} - {values}')
        for i in values:
            new_sum(i)
    # если словарь(dict) - рекурсия по значению и по ключам
    elif isinstance(values, dict):
        print(f'длинна словаря -{len(values)} - {values}')
        for key, val in values.items():
            new_sum(val)
    # если строковое значение суммируем длину строк
    elif isinstance(values, str):
        print(f'длина строки - {len(values)} - {values}')
        len_str += len(values)

    return

def main():
    new_sum(data_structure)

    print(f'Сумма чисел - {sum_}, сумма строк - {len_str}, всего - {sum_ + len_str}')


if __name__ == '__main__':
    main()