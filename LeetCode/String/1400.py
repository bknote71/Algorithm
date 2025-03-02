from collections import defaultdict


class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        # 홀수 개수
        # 짝수 개수

        count = defaultdict(int)

        for char in s:
            count[char] += 1

        odd_count = 0
        even_count = 0

        for key in count.keys():
            odd_count += count[key] & 1
            even_count += (count[key] - (count[key] & 1)) // 2

        return odd_count <= k and (odd_count + 2 * even_count) >= k


print(Solution().canConstruct("qlkzenwmmnpkopu", 15))
