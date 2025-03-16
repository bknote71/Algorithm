N = int(input())
arr = list(input().split())


left = [0] * N
vst = {}

for i in range(N):
    vst[arr[i]] = True
    left[i] = len(vst.keys())


right = [0] * N
rvst = {}

for i in range(N - 1, -1, -1):
    rvst[arr[i]] = True
    right[i] = len(rvst.keys())

answer = 0
for i in range(N - 1):
    answer = max(answer, left[i] + right[i + 1])

print(answer)
