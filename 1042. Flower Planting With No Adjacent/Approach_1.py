from collections import defaultdict

class Solution:
    def gardenNoAdj(self, n: int, paths: list[list[int]]) -> list[int]:
        adj = defaultdict(list)
        for x, y in paths:
            adj[x].append(y)
            adj[y].append(x)

        answer = [0] * (n + 1)

        for i in range(1, n + 1):
            used_colors = set()
            for neighbor in adj[i]:
                if answer[neighbor] != 0:
                    used_colors.add(answer[neighbor])

            for flower_type in range(1, 5):
                if flower_type not in used_colors:
                    answer[i] = flower_type
                    break
        
        return answer[1:]