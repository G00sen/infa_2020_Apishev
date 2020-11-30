a = list(map(int, input().split()))
z = []
for i in a:
    if i > 0:
        z += [i]
print(min(z))
