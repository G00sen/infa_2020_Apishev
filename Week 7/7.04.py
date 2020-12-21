inFile = open('input.txt', 'r', encoding='utf-8')
a = list(map(str, inFile.read().split()))
s = set(a)
print(len(s))
