my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
i = -1
while True:
    i += 1
    if i > len(my_list)-1 or my_list[i] < 0:
        break
    elif  my_list[i] == 0:
        continue
    elif my_list[i] >= 0:
        print(my_list[i])