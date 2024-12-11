class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i : [] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        def dfs(node, visited):
            if node in visited:
                return
            visited.add(node)
            for nbr in graph[node]:
                dfs(nbr, visited)

        components = 0
        visited = set()
        for i in range(n):
            if i in visited:
                continue
            dfs(i, visited)
            components += 1

        return components


