"""
Your task, is to create a NxN spiral with a given size.

For example, spiral with size 5 should look like this:

11111
....1
111.1
1...1
11111
Return value should contain array of arrays, of '.' and 1.
General rule-of-a-thumb is, that the snake made with '1' cannot touch to itself.
"""

def spiral(n):
    matrix = [['.' if j != n-1 else 1 for j in range(n)] if i not in (0, n-1) else [1 for i in range(n)] for i in range(n)]
    i_temp, j_temp = n - 1, 0
    mode = 'Up'
    cnt = 2
    while n - cnt > 1:
        if mode == 'Up':
            for i in range(i_temp, i_temp - (n - cnt), -1):
                matrix[i][j_temp] = 1
            mode = 'Right'; i_temp = i
        elif mode == 'Right':
            for j in range(j_temp, j_temp + (n - cnt)):
                matrix[i_temp][j] = 1
            cnt += 2
            mode = 'Down'; j_temp = j
        elif mode == 'Down':
            for i in range(i_temp, i_temp + (n - cnt)):
                matrix[i][j_temp] = 1
            mode = 'Left'; i_temp = i
        elif mode == 'Left':
            for j in range(j_temp, j_temp - (n - cnt), -1):
                matrix[i_temp][j] = 1
            cnt += 2
            mode = 'Up'; j_temp = j
    if n % 2 == 0: matrix[i_temp][j_temp] = '.'
    return matrix


n = int(input('Введите число: '))
for line in spiral(n):
    print(*line)
