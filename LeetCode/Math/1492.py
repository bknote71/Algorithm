class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        left = []
        right = []

        for i in range(1, int(n ** (1 / 2)) + 1):
            if n % i == 0:
                left.append(i)
                if n // i != i:
                    right.append(n // i)

        if len(left) + len(right) < k:
            return -1

        if len(left) >= k:
            return left[k - 1]
        else:
            t = k - len(left)
            return right[len(right) - t]


print(Solution().kthFactor(12, 5))
