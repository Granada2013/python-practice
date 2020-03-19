"""
Your task, is to create a NxN spiral with a given size.

For example, spiral with size 5 should look like this:

00000
....0
000.0
0...0
00000
Return value should contain array of arrays, of 0 and 1, for example for given size 5 result should be:
[[1,1,1,1,1],[0,0,0,0,1],[1,1,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Because of the edge-cases for tiny spirals, the size will be at least 5.
General rule-of-a-thumb is, that the snake made with '1' cannot touch to itself.
"""

def spiral(n):
    matrix = [[0 if j != n-1 else 1 for j in range(n)] if i not in (0, n-1) else [1 for i in range(n)] for i in range(n)]
    i_temp, j_temp = n - 1, 0
    mode = 'Up'
    cnt = 1
    while n - cnt*2 > 1:
        if mode == 'Up':
            for i in range(i_temp, i_temp - (n - cnt * 2), -1):
                matrix[i][j_temp] = 1
            mode = 'Right'; i_temp = i
        elif mode == 'Right':
            for j in range(j_temp, j_temp + (n - cnt * 2)):
                matrix[i_temp][j] = 1
            cnt += 1
            mode = 'Down'; j_temp = j
        elif mode == 'Down':
            for i in range(i_temp, i_temp + (n - cnt * 2)):
                matrix[i][j_temp] = 1
            mode = 'Left'; i_temp = i
        elif mode == 'Left':
            for j in range(j_temp, j_temp - (n - cnt * 2), -1):
                matrix[i_temp][j] = 1
            cnt += 1
            mode = 'Up'; j_temp = j
    if n % 2 == 0: matrix[i_temp][j_temp] = 0
    return matrix



