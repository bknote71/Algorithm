import sys

from collections import defaultdict

sys.setrecursionlimit(10**6)

N, K = map(int, input().split())

tree = defaultdict(list)

for _ in range(N * K - 1):
    u, v = map(int, input().split())
    tree[u - 1].append(v - 1)
    tree[v - 1].append(u - 1)

# 리프노드에서부터 시작하여 K개를 묶어 잘라낸다.

# 아래에서 올라오는 경로
# 경로의 개수


def dfs(v, p):
    total = 1

    brances = 0

    for u in tree[v]:
        if u == p:
            continue

        subtree_size = dfs(u, v)
        total += subtree_size % K
        if subtree_size % K > 0:
            brances += 1

    # 이때의 브렌치는 N개 묶인 것을 제외
    if brances >= 3:
        print("No")
        sys.exit()

    if total > K:
        print("No")
        sys.exit()

    if total < K and brances >= 2:
        print("No")
        sys.exit()

    return total


dfs(0, -1)
print("Yes")
