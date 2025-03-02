from collections import Counter


class Solution:
    def largestInteger(self, nums: list[int], k: int) -> int:
        count = Counter()

        for i in range(len(nums) - k + 1):
            count.update(set(nums[i : i + k]))

        return max((num for num in count if count[num] == 1), default=-1)


print(Solution().largestInteger([0, 0], 2))
