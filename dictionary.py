
# Словарь - имеет ключ и значение (2 переменных)
#phone_book = {"Denis": 89132045544, "Oleg": 89772030506}
#phone_book["Anton"] = 89663335456
# Если значение по ключу отсутствует происходит добавление в конце словаря
#print(phone_book)
# del phone_book['Oleg']
#phone_book.update({"Saha" : 89995556464,
#                   "Alex" : 87775006464})
#print(phone_book.get('Timur', 'Такого ключа нет!')) # Не выдает ошибку при отсутствии ключа!!!
# phone_num = phone_book.pop('Anton') # Извлекает из словаря пару по ключу
# print(phone_num)                    # присваивае переменной значение.
#print(phone_book)
# print(phone_book.keys()) # Список ключей
# print(phone_book.values()) # Список значений
#print(phone_book.items()) # Возвращает пары
# dict_items([('Denis', 89132045544), ('Oleg', 89772030506), ('Anton', 89663335456),
# ('Saha', 89995556464), ('Alex', 87775006464)])

# Множество хранит только уникальное значение
set_ = {1,2,3,4,5,1,2,3,4}
list_ = [1,1,1,2,3,3,3]
list_ = set(list_)
print(list_)
print(set_)
# Методы «discard» и «remove» - для удаления
set_.discard(5)
print(set_)
set_.add(6)
print(set_)