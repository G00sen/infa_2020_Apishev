n = int(input())
i = 2
s = 1
while i != n + 1:
    s += 1/(i**2)
    i += 1
print(s)
