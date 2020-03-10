n = int(input())
dic = set()
for _ in range(n):
    dict.add(input())
m = int(input())
text = ''
row_w = ''
for row in range(m):
    line = input()
    if row_w == '':
        text += line + ' '
        line = line.split()
        for word in line:
            for w in dic:
                if w in word:
                    row_w = row + 1
                    ind = text.split().index(word)
                    break
if row_w == '':
    print('Passed')
else:
    print(row_w, ind)



