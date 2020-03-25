"""
Найти самую длинную субпоследовательность, которая больше всего раз повторяется в заданной строке.
Если таких субпоследовательностей несколько - вывести любую из них.
"""
s = input()
d = dict()
for i in range(0, len(s) - 1):
    word = s[i]
    for j in range(i + 1, len(s)):
        word += s[j]
        d[word] = 1 + s[:i].count(word) + s[j:].count(word)
l = [value for value in d.values()]
a = max(l)
l = [key for key in d.keys() if d[key] == a]
l.sort(key = lambda x: len(x), reverse = True)
print(l[0], d[l[0]])




