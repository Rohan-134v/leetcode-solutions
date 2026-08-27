# 200. Number of Islands

### Difficulty: Medium

## Description
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 
Example 1:


Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1


Example 2:


Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3


 
Constraints:


	m == grid.length
	n == grid[i].length
	1 <= m, n <= 300
	grid[i][j] is '0' or '1'.

## Submission Details
- **Status**: Accepted
- **Runtime**: 223
- **Memory**: 21528000
- **Language**: python3

## Code
```python3
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: 
            return 0
        len_row = len(grid)
        len_col = len(grid[0])
        count = 0
        def dfs(r,c):
            if r < 0 or r >= len_row or c < 0 or c >= len_col or grid[r][c] == '0':
                return 
            
            grid[r][c] = '0'

            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c-1)
            dfs(r,c+1)

        for r in range(len_row):
            for c in range(len_col):
                if grid[r][c] == '1':
                    count += 1
                    dfs(r,c)
        return count


```
