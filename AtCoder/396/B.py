Q = int(input())
stack = [0] * 100

for i in range(Q):
    query = list(map(int, input().split()))
    if len(query) > 1:
        stack.append(query[1])
    else:
        print(stack.pop())
