from collections import defaultdict


class Solution:
    def minZeroArray(self, nums: list[int], queries: list[list[int]]) -> int:
        # 정확히 val만큼 깎아야 함.
        # 필수로 포함시켜야 하는 쿼리 셋들을 인덱스별 검색
        # 거기서 제일 이후의 쿼리 인덱스가 답

        # 쿼리 vali 를 누적해서 더하는 방법?
        # 누적해서 더한다고는 하지만, 사실상 nums[i]부터 0까지 키로해서 탐색한 후 존재한다면 그거 + vali
        # 그 값이 nums[i]라면 찾은 것.

        n = len(nums)
        required_queries = [-1] * n
        accumulated = [{} for _ in range(n)]

        for i in range(n):
            accumulated[i][0] = True

        for query_idx, (li, ri, vali) in enumerate(queries):

            for i in range(li, ri + 1):
                for target in range(nums[i], -1, -1):
                    if target in accumulated[i]:
                        accumulated[i][target + vali] = True

                if nums[i] in accumulated[i] and required_queries[i] == -1:
                    required_queries[i] = query_idx

        if any(nums[i] not in accumulated[i] for i in range(n)):
            return -1

        return max(required_queries) + 1


# print(Solution().minZeroArray([2, 0, 2], [[0, 2, 1], [0, 2, 1], [1, 1, 3]]))
print(
    Solution().minZeroArray(
        [10], [[0, 0, 4], [0, 0, 8], [0, 0, 1], [0, 0, 10], [0, 0, 10]]
    )
)
