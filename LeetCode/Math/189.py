class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n

        # 1. n - k ~ n - 1까지 temp_arr에 기록
        # 2. 0 ~ n - k - 1까지 nums에 끝으로 밀기
        # 3. temp_arr를 채우기

        temp_arr = nums[n - k :]

        for i in range(n - k - 1, -1, -1):
            nums[i + k] = nums[i]

        for i in range(k):
            nums[i] = temp_arr[i]


Solution().rotate([1, 2, 3, 4, 5, 6, 7], 3)
