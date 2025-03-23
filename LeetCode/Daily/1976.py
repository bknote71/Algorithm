from collections import defaultdict


class Solution:
    def countPaths(self, n: int, roads: list[list[int]]) -> int:
        # dfs(cur)
        #   if cur == last: return 0
        #
        # if dp[0][cur] + dp[next][n - 1]:
        #   total += dfs(next)

        inf = float("inf")

        graph = [[inf] * n for _ in range(n)]

        for i in range(n):
            graph[i][i] = 0

        for u, v, time in roads:
            graph[u][v] = time
            graph[v][u] = time

        def floyd_warshall():
            for k in range(n):
                for i in range(n):
                    for j in range(n):
                        if graph[i][j] > graph[i][k] + graph[k][j]:
                            graph[i][j] = graph[i][k] + graph[k][j]

        floyd_warshall()

        mod = 10**9 + 7
        dp = {}

        # print(graph[0][n - 1], times)

        def dfs(cur):
            if cur == n - 1:
                return 1

            if cur in dp:
                return dp[cur]

            total = 0

            for i in range(n):
                if cur == i or graph[cur][i] == inf:
                    continue

                if (graph[0][cur] + graph[(cur, i)] + graph[i][n - 1]) == graph[0][n - 1]:
                    total = (total + dfs(i)) % mod

            dp[cur] = total
            return total

        return dfs(0)


print(
    Solution().countPaths(
        7,
        [
            [0, 6, 7],
            [0, 1, 2],
            [1, 2, 3],
            [1, 3, 3],
            [6, 3, 3],
            [3, 5, 1],
            [6, 5, 1],
            [2, 5, 1],
            [0, 4, 5],
            [4, 6, 2],
        ],
    )
)
