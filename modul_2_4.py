# Определение простого и составного числа из указаного диапазона
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []  # Активация переменной типа List
not_primes = []

for i in range(len(numbers)):
    if numbers[i] < 2:  # Не учитываем число 1 так как не является простым.
        continue
    is_primes = True
    for j in range(i):
        # Если число делится без остатка (кроме 1 и самого себя) - значит составное
        if numbers[i] % numbers[j] == 0 and numbers[j] > 1:
            is_primes = False
            break
    if is_primes:
        primes.append(numbers[i])
    else:
        not_primes.append(numbers[i])

print("Primes:", primes)
print("Not Primes:", not_primes)
