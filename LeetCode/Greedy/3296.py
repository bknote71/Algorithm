class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: list[int]) -> int:
        def canReduceToZero(T):
            total_reduced = 0
            for time in workerTimes:
                lo, hi = 0, int(1e6)
                while lo + 1 < hi:
                    mid = (lo + hi) // 2
                    if (mid * (mid + 1) // 2) * time <= T:
                        lo = mid
                    else:
                        hi = mid
                total_reduced += lo

            return total_reduced >= mountainHeight

        lo, hi = 0, int(1e10)
        while lo + 1 < hi:
            mid = (lo + hi) // 2
            if canReduceToZero(mid):
                hi = mid
            else:
                lo = mid

        print(lo, hi)

        return hi


Solution().minNumberOfSeconds(4, [2, 1, 1])
