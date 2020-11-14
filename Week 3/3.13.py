s = str(input())
blank = s.find(' ')
news = s[blank + 1:] + ' ' + s[:blank]
print(news)
