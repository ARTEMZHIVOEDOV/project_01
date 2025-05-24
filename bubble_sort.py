a = [6, 4, 8, 4, 1, 5, 7, 10, -5, -7, -3]

N = len(a)
for i in range(N-1):
    for i in range(N-1):
        if a[i] > a[i+1]:
            a[i], a[i+1] = a[i+1], a[i]

    print(a)


print('Текст из ветки test branch 2')