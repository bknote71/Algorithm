import math


class Solution:
    def repairCars(self, ranks: list[int], cars: int) -> int:
        # 시간을 찾는 파라미터 서치
        # FFTT
        lo, hi = 0, max(ranks) * cars**2
        while lo + 1 < hi:
            mid = (lo + hi) // 2
            total = 0
            for rank in ranks:
                cand = int(math.sqrt(mid // rank))
                total += cand

            if total >= cars:
                hi = mid
            else:
                lo = mid

        return hi


Solution().repairCars([4, 2, 3, 1], 10)
