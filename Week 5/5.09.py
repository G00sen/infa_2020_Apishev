a = list(map(int, input().split()))
for i in range(1, len(a)):
    if a[i] > a[i - 1]:
        print(a[i], end=' ')
