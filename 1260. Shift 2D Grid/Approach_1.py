class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        res = [[0] * n for _ in range(m)]
        
        for r in range(m):
            for c in range(n):
                new_val = (r * n + c + k) % (m * n)
                new_r, new_c = new_val // n, new_val % n
                res[new_r][new_c] = grid[r][c]
                
        return res