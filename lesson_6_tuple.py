#Коотеж - не изменяемый список, упорядоченный
tuple_ = 1,2,3,4,True, "Strings"
print(tuple_)
tuple_2 = tuple(["Денис","Борис","Андрей","Вадим"])
line_2 = ["Денис","Борис","Андрей","Вадим"]
print(tuple_2)
print(tuple_2.__sizeof__())
print(line_2.__sizeof__())

tuple_ = (1,[1,3,5,7], 2, 4) + tuple_2
print(tuple_)
tuple_[1][1]=2
print(tuple_)