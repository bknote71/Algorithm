N = int(input())

# x^3 - y^3 = N
# (x - y)(x^2 + xy + y^2)

# x - y = k (x = y + k)

# 1. N >= (x - y)(x^2 - 2xy + y^2) = (x - y)^3
# k^3 <= N

# k(3y^2 + 3yk + k^2) == N
# (3y^2 + 3yk + k^2) == N // k (N % k == 0)

# find k, y
# 3y^2 + 3yk + k^2 - N // k == 0


def bs(k, m):
    lo, hi = 0, 600000001
    while lo + 1 < hi:
        y = (lo + hi) // 2

        if (3 * y**2 + 3 * y * k + k**2 - m) <= 0:
            lo = y
        else:
            hi = y

    if (3 * lo**2 + 3 * lo * k + k**2 - m) == 0:
        return lo

    return -1


def solve():
    k = 1
    while k**3 <= N:
        if N % k == 0:
            m = N // k
            y = bs(k, m)
            if y > 0:
                return (y + k, y)

        k += 1

    return (-1, -1)


x, y = solve()
if x != -1:
    print(x, y)
else:
    print(-1)
