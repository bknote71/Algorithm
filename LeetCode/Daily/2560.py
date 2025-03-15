class Solution:
    def minCapability(self, nums: list[int], k: int) -> int:
        n = len(nums)
        lo, hi = 0, max(nums)
        while lo + 1 < hi:
            mid = (lo + hi) // 2

            cnt = 0
            idx = 0
            while idx < n:
                if nums[idx] <= mid:
                    cnt += 1
                    idx += 1
                idx += 1

            if cnt >= k:
                hi = mid
            else:
                lo = mid

        return hi
