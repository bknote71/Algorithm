# (적은)모든 요소에 대해, 특정 요소가 각 구간에서 몇 개 있는지 알기: O(Q log N) (Q: 구간개수, N: 구간길이)
# 1. 각 요소가 등장하는 인덱스를 기록 (0..n-1)
# 2. 주어진 구간 [l, r]에 대해 이분탐색으로 몇 개의 요소가 있는지 탐색 가능.


class Solution:
    def sameEndSubstringCount(self, s: str, queries: list[list[int]]) -> list[int]:
        answer: list[int] = []

        return answer
