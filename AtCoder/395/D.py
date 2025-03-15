import sys


N, Q = map(int, input().split())

pigeon = list(range(N + 1))
rnest = list(range(N + 1))
vnest = list(range(N + 1))

for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        pigeon[q[1]] = q[2]
    elif q[0] == 2:

        rnest[q[1]], rnest[q[2]] = rnest[q[2]], rnest[q[1]]

    else:
        print(rnest[pigeon[q[1]]])
