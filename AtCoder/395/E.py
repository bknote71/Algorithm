from collections import defaultdict
import heapq

graph = defaultdict(list)
rgraph = defaultdict(list)

N, M, X = map(int, input().split())
for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    rgraph[v].append(u)


# 다익스트라?
# - 상태: node + 뒤집기 여부
def dijkstra():
    inf = float("inf")
    distance = [[inf] * 2 for _ in range(N + 1)]
    distance[1][0] = 0

    pq = [(0, 1, 0)]

    while pq:
        dist, node, state = heapq.heappop(pq)

        if distance[node][state] < dist:
            continue

        g = graph if state == 0 else rgraph
        for ne in g[node]:
            if dist + 1 < distance[ne][state]:
                distance[ne][state] = dist + 1
                heapq.heappush(pq, (dist + 1, ne, state))

        # 뒤집기
        nstate = 1 - state
        if dist + X < distance[node][nstate]:
            distance[node][nstate] = dist + X
            heapq.heappush(pq, (dist + X, node, nstate))

    return min(distance[N][0], distance[N][1])


print(dijkstra())
