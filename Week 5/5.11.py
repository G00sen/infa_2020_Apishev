n = int(input())
a = list(map(int, input().split()))
b = []
n1 = int(input())
for i in range(n):
    b.append(abs(a[i]-n1))
print(a[b.index(min(b))])
