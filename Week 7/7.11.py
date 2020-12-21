file = open('input.txt', 'r', encoding='utf8')
fileOut = open('output.txt', 'w', encoding='utf8')
input_data = file.readlines()

candidaty = dict()
putin = list()
for l in input_data:
    candidaty[l] = candidaty.get(l, 0) + 1
for l in candidaty:
    putin.append((candidaty[l], l))
putin = sorted(putin)
if putin[-1][0] > len(input_data) / 2:
    fileOut.writelines(putin[-1][1])
else:
    fileOut.writelines(putin[-1][1])
    fileOut.writelines(putin[-2][1])
