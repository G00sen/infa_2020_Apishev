from math import *

x = float(input())
if x > 1:
    a = floor(x)
    b = x - a
    print(round(b, 2))
else:
    print(x)
