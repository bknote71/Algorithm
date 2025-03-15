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

    parts = []

    while q:
        cur = q.popleft()
        parts.append(cur)

        for next, w in graph[cur]:
            if not vst[next]:
                A[next] = A[cur] ^ w
                vst[next] = True
                q.append(next)

            elif A[next] != (A[cur] ^ w):
                failure = True
                return []

    return parts


def solve():
    for i in range(1, N + 1):
        if vst[i]:
            continue

        parts = bfs(i)

        if failure:
            return

        pn = len(parts)
        we = 0

        for i in range(61):
            ocount = 0
            for part in parts:
                ocount += 1 if A[part] & (1 << i) else 0

            if ocount > pn - ocount:
                we |= 1 << i

        for part in parts:
            A[part] ^= we


solve()

if failure:
    print(-1)
else:
    for i in range(1, N + 1):
        print(A[i], end=" ")
