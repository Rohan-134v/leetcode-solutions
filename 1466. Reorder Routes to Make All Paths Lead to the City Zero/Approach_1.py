class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj = [ []  for _ in range(n)]

        for u, v in connections:
            adj[u].append((v,1))
            adj[v].append((u,0))

        visit = {0}
        stack = [0]
        reverse = 0
        while stack:
            city = stack.pop()
            for neigh, cost in adj[city]:
                if neigh not in visit:
                    visit.add(neigh)
                    reverse += cost
                    stack.append(neigh)
        return reverse