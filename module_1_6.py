print("# Словарь")
my_dict = {'Igor': 1977, 'Vadim': 1975, 'Vladimir': 1939, 'Oleg':1961}
print(my_dict)
print(my_dict['Vadim'])
print(my_dict.get('Aleks','Такого значения нет.'))
my_dict.update({'Oksana': 1988,
                'Elena': 1979})
year_birth = my_dict.pop('Igor')
print(year_birth)
print(my_dict)
print("#")
print("# Множество")
print("#")
my_set = {1,3,4,True,"Map","Speed",2,5,4,3, "Map"}
print(my_set)
my_set.add((1,7,8))
my_set.add(8)
print(my_set)