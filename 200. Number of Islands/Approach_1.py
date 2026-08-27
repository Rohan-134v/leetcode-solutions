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

