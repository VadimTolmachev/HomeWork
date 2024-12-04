def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [4, 5, 9]
print_params(*values_list)

values_list = [3.14, 'Пример!']
print_params(*values_list, 'Стоп')

values_dict = {'a': 2, 'b': 3, 'c': 4}
print_params(**values_dict)
