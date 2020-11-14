a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())
if d != 0:
    y = (e * c - f * a) / (c * b - a * d)
    if a != 0:
        x = (e - b * y) / a
        print(float(x), float(y))
elif c != 0:
    x = (e * d - f * b) / (a * d - b * c)
    if b != 0:
        y = (e - a * x) / b
        print(float(x), float(y))
