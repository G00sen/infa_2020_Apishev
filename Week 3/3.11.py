s = str(input())
first = s.find('h')
rev = s[::-1]
last = rev.find('h')
last = len(s) - last - 1
news = s[:first] + s[last + 1:]
print(news)
