from collections import defaultdict
from collections import deque

N, M = map(int, input().split())
A = [-1] * (N + 1)  # all 1

graph = defaultdict(list)

for i in range(M):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))
    graph[y].append((x, z))


vst = [False] * (N + 1)
failure = False


def bfs(cur):
    global failure
    q = deque([cur])
    A[cur] = 0
    vst[cur] = True

    while q:
        cur = q.popleft()

        for next, w in graph[cur]:
            if not vst[next]:
                A[next] = A[cur] ^ w
                vst[next] = True
                q.append(next)

            elif A[next] != (A[cur] ^ w):
                failure = True
                return


def solve():
    for i in range(1, N + 1):
        if not vst[i]:
            bfs(i)

        if failure:
            return


solve()

if failure:
    print(-1)
else:
    for i in range(1, N + 1):
        print(A[i], end=" ")
