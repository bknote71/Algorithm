N = int(input())
A = list(map(int, input().split()))


def solve():
    for i in range(len(A) - 1):
        if A[i] >= A[i + 1]:
            return False

    return True


print("Yes" if solve() else "No")
