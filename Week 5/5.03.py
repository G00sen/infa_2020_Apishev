n = int(input())
first_string = '+___ ' * n
second_string = ''

for i in range(1, n + 1):
    second_string += '|' + str(i) + ' / '

third_string = '|__\\ ' * n
fourth_string = '|    ' * n

for i in (first_string, second_string, third_string, fourth_string):
    print(i)
