grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = sorted(list(students))
x = 0
dict_grades = {}
for i in students:
    avg = sum(grades[x]) / len(grades[x])
    print(i, avg)
    dict_grades[i] = avg
    x += 1

print(dict_grades)
