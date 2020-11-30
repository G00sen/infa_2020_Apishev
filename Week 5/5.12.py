numList = list(map(int, (input().split())))

for i in range(1, len(numList)):
    if i % 2 == 1:
        numList.insert(i - 1, numList.pop(i))

print(' '.join(map(str, numList)))
