import math

a = float(input())
b = float(input())
c = float(input())

D = b ** 2 - 4 * a * c

if D > 0 and a > 0:
    x1 = (- b - math.sqrt(D)) / (2 * a)
    x2 = (- b + math.sqrt(D)) / (2 * a)
    print(round(x1, 6), round(x2, 6))
elif D > 0 and a < 0:
    x1 = (- b - math.sqrt(D)) / (2 * a)
    x2 = (- b + math.sqrt(D)) / (2 * a)
    print(round(x2, 6), round(x1, 6))
elif D == 0:
    x = - b / (2 * a)
    print(x)
