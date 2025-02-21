"""
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
"""

def num_islands(grid):
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    visited = set() #集合，用于存储已经访问过的网格坐标 (r, c)

    def dfs(r, c):
        if (r < 0 or c < 0 or r >= rows or c >= cols or
            grid[r][c] == 0 or (r, c) in visited):
            return
        visited.add((r, c))
        dfs(r - 1, c) #up
        dfs(r + 1, c) #down
        dfs(r, c - 1) #left
        dfs(r, c + 1) #right

    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and (r, c) not in visited:
                dfs(r, c)
                count += 1

    return count
        
'''
#另一种思路，把访问过的岛屿全部标记为0
def num_islands(grid):
    count = 0
    for i in range(len(grid)):
        for j, col in enumerate(grid[i]): # enumerate(grid[i]) 让j获取索引，col获取当前单元格的值0或者1。enumerate()作用：同时获取索引和值，替代 range(len())
            if col == 1:
                dfs(grid, i, j)
                count += 1
    return count


def dfs(grid, i, j):
    if (i < 0 or i >= len(grid)) or (j < 0 or j >= len(grid[0])):
        return
    if grid[i][j] != 1:
        return
    grid[i][j] = 0
    dfs(grid, i+1, j)
    dfs(grid, i-1, j)
    dfs(grid, i, j+1)
    dfs(grid, i, j-1)
'''
