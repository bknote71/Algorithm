class Solution:
    def longestPalindromicSubsequence(self, s: str, k: int) -> int:
        n = len(s)
        dp = {}

        def dfs(i, j, k):
            if i > j:
                return 0
            if i == j:
                return 1

            if (i, j, k) in dp:
                return dp[(i, j, k)]

            if s[i] == s[j]:
                dp[(i, j, k)] = 2 + dfs(i + 1, j - 1, k)
                return dp[(i, j, k)]

            result = 0

            diff = min(abs(ord(s[i]) - ord(s[j])), 26 - abs(ord(s[i]) - ord(s[j])))
            if k >= diff:
                result = max(result, 2 + dfs(i + 1, j - 1, k - diff))

            result = max(result, dfs(i + 1, j, k))
            result = max(result, dfs(i, j - 1, k))

            dp[(i, j, k)] = result
            return result

        return dfs(0, n - 1, k)
