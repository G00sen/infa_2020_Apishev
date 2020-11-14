string = input()
firstI = string.find('f')
reverse = string[::-1]
lastI = len(string) - reverse.find('f') - 1
if firstI == lastI:
    print(firstI)
elif firstI == -1 or lastI == -1:
    print('')
else:
    print(firstI, lastI)
