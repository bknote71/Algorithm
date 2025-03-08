class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        answer = 1

        N, M = max(m, n), min(m, n)

        # (N+M-2)Comb(N-1)

        for i in range(M - 1):
            answer *= N + M - 2 - i

        for i in range(M - 1):
            answer //= i + 1

        return answer
