class Solution:
    def check(self, n, m, edges):
        adj = [[] for _ in range(n + 1)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(cur, visited, cnt):
            if cnt == n:
                return True

            for nxt in adj[cur]:
                if not visited[nxt]:
                    visited[nxt] = True
                    if dfs(nxt, visited, cnt + 1):
                        return True
                    visited[nxt] = False

            return False

        for start in range(1, n + 1):
            visited = [False] * (n + 1)
            visited[start] = True

            if dfs(start, visited, 1):
                return 1

        return 0
