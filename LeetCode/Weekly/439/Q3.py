class Solution:
    def maxSum(self, nums: list[int], k: int, m: int) -> int:
        n = len(nums)
        dp = {}

        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        inf = 2000000000

        def dfs(idx, kk):
            if kk == 0:
                return 0

            if idx >= n or (n - idx) < kk * m:
                return -inf

            if (idx, kk) in dp:
                return dp[(idx, kk)]

            result = dfs(idx + 1, kk)

            for j in range(idx + m - 1, n - (kk - 1) * m):
                cursum = prefix[j + 1] - prefix[idx]
                result = max(result, cursum + dfs(j + 1, kk - 1))

            dp[(idx, kk)] = result
            return result

        return dfs(0, k)


print(Solution().maxSum([1, 2, -1, 3, 3, 4], 2, 2))
print(Solution().maxSum([-2, -10, 15, 12, 8, 11, 5], 3, 2))
