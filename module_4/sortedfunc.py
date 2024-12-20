nums = [1, 4, 5, 3, 2, 7, 5, 9, 6, 8, 0]


# Пузырьковая функция сортировки
def bubble_sort(ls):
    swapped = True
    count1 = 0
    while swapped:
        swapped = False
        count1 += 1
        for i in range(len(ls) - 1):
            if ls[i] > ls[i + 1]:
                ls[i], ls[i + 1] = ls[i + 1], ls[i]
                swapped = True
    return count1


# Функция сортировки перебором
def selection_sort(ls):
    for i in range(len(ls)):
        lowest = i
        for j in range(i + 1, len(ls)):
            if ls[j] < ls[lowest]:
                lowest = j
        ls[i], ls[lowest] = ls[lowest], ls[i]


if __name__ == '__main__':
    # print(bubble_sort(nums))
    # print(nums)
    selection_sort(nums)
    print(nums)
