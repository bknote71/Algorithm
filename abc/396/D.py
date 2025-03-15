from collections import defaultdict

N, M = map(int, input().split())

graph = defaultdict(list)

for i in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

vst = [False] * (N + 1)

answer = float("inf")


def dfs(cur, xorvalue):

    if cur == N:
        global answer
        answer = min(answer, xorvalue)
        return

    vst[cur] = True

    for next, w in graph[cur]:
        if not vst[next]:
            dfs(next, xorvalue ^ w)

    vst[cur] = False


dfs(1, 0)
print(answer)
