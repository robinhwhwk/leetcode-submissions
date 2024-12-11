class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # a tree is invalid when there is a cycle
        adj_list = {i: [] for i in range(n)}
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        def dfs(parent, node, visited):
            visited.add(node)
            for nbr in adj_list[node]:
                if nbr not in visited:
                    if dfs(node, nbr, visited):
                        return True
                elif nbr in visited and nbr != parent:
                    return True
            return False
        visited = set([])
        if dfs(-1, 0, visited):
            return False
        if len(visited) != n:
            return False

        return True
