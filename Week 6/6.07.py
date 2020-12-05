count = int(input())
i = 0
myList = []
while i < count:
    newList = list(map(str, input().split()))
    newList[1] = int(newList[1])
    myList.append(tuple(newList))
    i += 1
myList.sort(key=lambda x: (-x[1]))
for i in myList:
    print(i[0])
