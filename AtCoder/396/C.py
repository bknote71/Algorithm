N, M = map(int, input().split())
B = list(map(int, input().split()))
W = list(map(int, input().split()))

B.sort(reverse=True)
W.sort(reverse=True)

answer = 0
bcnt = 0
wcnt = 0

for i in range(N):
    if B[i] < 0:
        bcnt = i
        break
    answer += B[i]


for j in range(M):
    if bcnt <= j or W[j] < 0:
        wcnt = j
        break

    answer += W[j]

while bcnt < N and wcnt < M:
    if B[bcnt] + W[wcnt] > 0:
        answer += B[bcnt] + W[wcnt]
        bcnt += 1
        wcnt += 1
    else:
        break

print(answer)
