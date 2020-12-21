n, slova = int(input()), dict()
for k in range(n):
    c = input()
    index = c.find(' ')
    slova[c[:index]], slova[c[index + 1:]] = c[index + 1:], c[:index]
print(slova[input()])
