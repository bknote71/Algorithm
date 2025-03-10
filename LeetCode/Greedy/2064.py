# 파라미터 서치


class Solution:
    def minimizedMaximum(self, n: int, quantities: list[int]) -> int:
        if sum(quantities) <= n:
            return 1

        lo, hi = -1, max(quantities)

        while lo + 1 < hi:
            mid = (lo + hi) // 2

            cand = 0

            if mid != 0:
                for q in quantities:
                    cand += (q // mid) + (1 if q % mid != 0 else 0)

            if cand <= n:
                hi = mid
            else:
                lo = mid

        return hi


Solution().minimizedMaximum(
    100000,
    [4, 4, 4, 2, 4, 2, 4, 1, 5, 4, 5, 4, 1, 1, 2, 2, 4, 1, 1, 4, 5, 3, 3, 4, 1, 2],
)
