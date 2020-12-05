N = int(input())
myList = list(map(int, input().split()))
sortedList = sorted(myList)
print(' '.join(map(str, sortedList)))
