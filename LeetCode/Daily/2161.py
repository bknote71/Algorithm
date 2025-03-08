class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        less = []
        greater = []

        same = 0

        for num in nums:
            if num < pivot:
                less.append(num)
            elif num > pivot:
                greater.append(num)
            else:
                same += 1

        return less + [pivot] * same + greater
