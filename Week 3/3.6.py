p = int(input())
x = int(input())
y = int(input())
money_do = 100 * x + y
money_posle = int(money_do * (100 + p) / 100)
print(money_posle // 100, money_posle % 100)
