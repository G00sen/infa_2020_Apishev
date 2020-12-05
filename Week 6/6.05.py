fi = open('input.txt', 'r', encoding='utf8')
fo = open('output.txt', 'w', encoding='utf8')
f = list(fi.readlines())
n = 0
while n < len(f):
    f[n] = f[n].split()
    n += 1
n = 0
while n < len(f):
    f[n] = f[n][0:2] + f[n][3:4]
    n += 1
n = 0
while n < len(f):
    f[n] = ' '.join(f[n])
    n += 1
n = 0
f.sort()
for i in range(len(f)):
    fo.write(f[i] + '\n')
