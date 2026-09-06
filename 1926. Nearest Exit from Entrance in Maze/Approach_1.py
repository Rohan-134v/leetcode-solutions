class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        q = deque()
        q.append((entrance[0], entrance[1], 0))
        directions = [(0, -1), (-1, 0), (0, 1), (1,0)]
        maze[entrance[0]][entrance[1]] = '+'
        while q:
            r,c, steps = q.popleft()
            if r == 0 or r == m -1 or c == 0 or c == n -1:
                if [r,c] != entrance:
                    return steps
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0<=nr<m and 0<=nc<n and maze[nr][nc]!= '+':
                    maze[nr][nc]  = '+'
                    q.append((nr, nc, steps+1))
        return -1
