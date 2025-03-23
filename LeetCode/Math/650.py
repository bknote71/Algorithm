# 참고) 등비수열의 합
# S = 1 + 2 + 4 + .. + 2^k 는 등비수열의 합이다.
#  (n = 0~k) sigmal(2^n)

# S = (r^(n + 1) - 1) / r - 1
# - r = 2, 항의 개수 k + 1개
# S = 2^(k+1) - 1


class Solution:
    def minSteps(self, n: int) -> int:
        # 약수

        dp = {}

        def dfs(x):
            if x == 1:
                return 0

            if x in dp:
                return x

            # 최악의 경우: 1씩 붙여넣기
            ret = x

            for i in range(2, x // 2 + 1):
                if x % i == 0:
                    ret = min(ret, dfs(i) + (x // i))

            dp[x] = ret
            return ret

        return dfs(n)


print(Solution().minSteps(3))
print(Solution().minSteps(6))
