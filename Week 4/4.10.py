def sum_seq(a):
    a = int(input())
    if a == 0:
        return 0
    answ = a + sum_seq(a)
    return answ
a = 0
print(sum_seq(a))
