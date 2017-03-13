list = ['' for x in range(17)]
i = 1
while i <= 9:
    j = 1
    while j <= i:
        sum = i * j
        str = '%s*%s=%s ' % (i, j, sum)
        if (i == 9):
            list[i - 1] += str
        else:
            list[i - 1] += str
            list[17 - i] += str
        j = j + 1
    i = i + 1


for item in list:
    print(item)
