class Solution:
    def maxSum(self, nums: list[int]) -> int:
        nums.sort(reverse=True)
        vst = {}
        answer = 0

        for num in nums:
            if num <= 0:
                break

            if num in vst:
                continue

            vst[num] = True
            answer += num

        if not vst:
            answer = nums[0]

        return answer


print(Solution().maxSum([-20, 20]))
