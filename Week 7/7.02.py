numbers1 = list(map(int, input().split()))
numbers2 = list(map(int, input().split()))
numbers1.sort()
numbers2.sort()
x = set(numbers1)
y = set(numbers2)
if len(x) <= len(y):
    x1 = list(x & y)
    x1.sort()
    print(*x1)
elif len(x) > len(y):
    y1 = list(y & x)
    y1.sort()
    print(*y1)
