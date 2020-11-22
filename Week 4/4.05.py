def IsPrime(n):
    d = 2
    while d * d <= n and n % d != 0:
        d += 1
    return d * d > n
n = int(input())
if IsPrime(n):
    print("YES")
else:
    print('NO')
