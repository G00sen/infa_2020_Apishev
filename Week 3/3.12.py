s = input()
i = s.find('f')
s1 = s[i + 1::]
i1 = s1.find('f')
if i1 == -1:
    if i == -1:
        print(-2)
    else:
        print(-1)
else:
    print(i1 + i + 1)
