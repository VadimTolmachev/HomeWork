immutable_var = (1, 2.0, True, "String")
print(immutable_var)
# immutable_var[0] = 2 # На этой строке возникает ошибка
# TypeError: 'tuple' object does not support item assignment
# Элементы кортежа менять нельзя

mutable_list = [1, 2, 3, True, "Hello!"]
mutable_list [0] = 3
print(mutable_list)