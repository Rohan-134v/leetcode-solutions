import collections
from typing import List

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = collections.defaultdict(list)
        for i in range(len(equations)):
            u, v = equations[i]
            val = values[i]

            adj[u].append((v, val))
            adj[v].append((u, 1.0 / val))

        def dfs(start, target):
            if start not in adj or target not in adj:
                return -1.0

            stack = [(start, 1.0)]
            visit = {start}

            while stack:
                node, curr = stack.pop()
                if node == target:
                    return curr
                for n, weight in adj[node]:
                    if n not in visit:
                        visit.add(n)
                        stack.append((n, curr * weight))
                
            return -1.0
                
        results = []
        for c, d in queries:
            results.append(dfs(c, d))
            
        return results