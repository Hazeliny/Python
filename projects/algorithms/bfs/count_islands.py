'''
This is a bfs-version of counting-islands problem in dfs section.
Given a 2d grid map of '1's (land) and '0's (water),
count the number of islands.
An island is surrounded by water and is formed by
connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

Example 1:
11110
11010
11000
00000
Answer: 1

Example 2:
11000
11000
00100
00011
Answer: 3

Example 3:
111000
110000
100001
001101
001100
Answer: 3

Example 4:
110011
001100
000001
111100
Answer: 5
'''

from collections import deque

def num_islands(grid):
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    islands = 0
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] #right, down, left, up

    def bfs(r, c):
        queue = deque([(r, c)])
        grid[r][c] = 0 #mark as visited

        while queue:
            row, col = queue.popleft() # 取出队列中的元素
            for dr, dc in directions: # 遍历四个方向
                nr, nc = row + dr, col + dc # 计算新的坐标
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    queue.append((nr, nc)) # 把新的陆地坐标加入队列
                    grid[nr][nc] = 0 #mark as visited

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1: #found a new island# 发现一个新的岛屿
                islands += 1
                bfs(r, c) # 进行BFS，将整个岛屿淹没

    return islands

'''
#无递归
def num_islands(grid):
    row = len(grid)
    col = len(grid[0])

    num_island = 0
    visited = [[0] * col for i in range(row)]
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    queue = []

    for i in range(row):
        for j, num in enumerate(grid[i]):
            if num == 1 and visited[i][j] != 1:
                visited[i][j] = 1
                queue.append((i, j))
                while queue:
                    x, y = queue.pop(0)
                    for k in range(len(directions)):
                        nx_x = x + directions[k][0]
                        nx_y = y + directions[k][1]
                        if nx_x >= 0 and nx_y >= 0 and nx_x < row and nx_y < col:
                            if visited[nx_x][nx_y] != 1 and grid[nx_x][nx_y] == 1:
                                queue.append((nx_x, nx_y))
                                visited[nx_x][nx_y] = 1
                num_island += 1
    return num_island
'''
