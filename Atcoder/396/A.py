N = int(input())
arr = list(input().split())


def solve():
    for i in range(N - 2):
        if arr[i] == arr[i + 1] == arr[i + 2]:
            print("Yes")
            return
    print("No")


solve()
