num_1 = [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]


for i in range(len(num_1)):
    divider = []
    the_summand = []
    for j in range(2, num_1[i]+1):
        if num_1[i] % j == 0:
            divider.append(j)
    #print(f'{num_1[i]} - {divider}')
    for j in range(len(divider)):
        a = divider[j] // 2
        x = 1
        while x <= a:
            the_summand.append(str(x) + '+' + str(divider[j] - x))
            x +=1
    the_summand = (sorted(the_summand))
    print(f'{num_1[i]} - {the_summand}')
