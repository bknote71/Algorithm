from collections import defaultdict
import heapq


class Solution:
    def countPaths(self, n: int, roads: list[list[int]]) -> int:
        # 다익스트라 + 최단경로 경우의 수
        # - 길이가 갱신될 때, 경우의 수를 갱신
        # - 길이가 동일하다면, 경우의 수에 합산

        mod = 10**9 + 7
        graph = defaultdict(list)

        for u, v, time in roads:
            graph[u].append((v, time))
            graph[v].append((u, time))

        inf = float("inf")

        dist = [inf] * n
        ways = [0] * n
        dist[0] = 0
        ways[0] = 1

        heap = [(0, 0)]  # (cost, node)

        while heap:
            cost, node = heapq.heappop(heap)

            if cost > dist[node]:
                continue

            for next, time in graph[node]:
                new_cost = cost + time

                if new_cost < dist[next]:
                    dist[next] = new_cost
                    ways[next] = ways[node]
                    heapq.heappush(heap, (new_cost, next))

                elif new_cost == dist[next]:
                    ways[next] = (ways[next] + ways[node]) % mod

        return ways[n - 1]
