k = int(input())


def MinDivisor(n):
    i = 0
    mindiv = 1
    while i <= n**0.5:
        if i != 0 and n % i == 0 and n // i < n:
            mindiv = i
            break
        else:
            mindiv = n
        i += 1
    return mindiv


print(MinDivisor(k))
