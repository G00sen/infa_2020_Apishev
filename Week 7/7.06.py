n = int(input())
languages = set()
all_languages = set()
language_set = set()
for i in range(n):
    language_set = set()
    N = int(input())
    for j in range(N):
        string = input()
        all_languages.add(string)
        language_set.add(string)
    languages.add(frozenset(language_set))
first = language_set
for i in languages:
    first &= i
others_lang = all_languages - first
print(len(first))
for i in first:
    print(i)
print(len(all_languages))
all_languages = list(all_languages)
all_languages.sort(reverse=True)
for i in all_languages:
    print(i)
