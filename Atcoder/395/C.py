from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

count = defaultdict(int)

left = 0
answer = len(A)
flag = False

for right in range(len(A)):
    count[A[right]] += 1

    while count[A[right]] > 1:

        flag = True
        answer = min(answer, right - left + 1)

        count[A[left]] -= 1
        left += 1

print(answer if flag else "-1")
