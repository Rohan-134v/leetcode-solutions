from typing import List
from collections import deque

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        hashmap = {}
        start = None
        count = 0

        for i in range(m):
            for j in range(n):
                if classroom[i][j] == 'S':
                    start = (i, j)
                elif classroom[i][j] == 'L':
                    hashmap[(i, j)] = count
                    count += 1
        
        if not start:
            return -1

        target = (1 << count) - 1

        queue = deque([(start[0], start[1], energy, 0, 0)])
        visited = {(start[0], start[1], 0): energy}
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while queue:
            r, c, currEnergy, mask, steps = queue.popleft()
            if mask == target:
                return steps
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < m and 0 <= nc < n and classroom[nr][nc] != 'X':
                    newEnergy = currEnergy - 1

                    if newEnergy < 0:
                        continue
                    
                    if classroom[nr][nc] == 'R':
                        newEnergy = energy
                    
                    nextMask = mask
                    if classroom[nr][nc] == 'L':
                        idx = hashmap[(nr, nc)]
                        nextMask |= (1 << idx)

                    if (nr, nc, nextMask) not in visited or newEnergy > visited[(nr, nc, nextMask)]:
                        visited[(nr, nc, nextMask)] = newEnergy
                        queue.append((nr, nc, newEnergy, nextMask, steps + 1))
                        
        return -1