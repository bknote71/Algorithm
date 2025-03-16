from collections import defaultdict

import bisect


class Solution:
    def solveQueries(self, nums: list[int], queries: list[int]) -> list[int]:
        indexes = defaultdict(list)

        for i, num in enumerate(nums):
            indexes[num].append(i)

        n = len(nums)
        answer = []

        for q in queries:
            # q번과 가장 가까우면서 nums[q]와 동일한
            arr = indexes[nums[q]]
            an = len(arr)
            if an == 1:
                answer.append(-1)
                continue

            pos = bisect.bisect_left(arr, q)
            min_dist = float("inf")

            if pos == 0 or pos == an - 1:
                min_dist = (arr[0] - arr[-1] + n) % n

            if pos > 0:
                min_dist = min(
                    min_dist, min(q - arr[pos - 1], (arr[pos - 1] - q + n) % n)
                )

            if pos < len(arr) - 1:
                min_dist = min(
                    min_dist, min(arr[pos + 1] - q, (q - arr[pos + 1] + n) % n)
                )

            answer.append(min_dist)

        return answer


# print(Solution().solveQueries([1, 3, 1, 4, 1, 3, 2], [0, 3, 5]))
print(Solution().solveQueries([14, 14, 4, 2, 19, 19, 14, 19, 14], [2, 4, 8, 6, 3]))
