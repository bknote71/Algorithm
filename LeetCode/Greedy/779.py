class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        curnum = 0
        x = 2 ** (n - 2)

        maps = {
            "0": "01",
            "1": "10",
        }

        # 만약 다음 선택이 왼쪽이면 계속
        # 아니라면 k -= x

        for i in range(n - 1):

            curnum = int(maps[str(curnum)][0 if k <= x else 1])
            if k > x:
                k -= x
            x >>= 1

        return curnum


print(Solution().kthGrammar(2, 1))
print(Solution().kthGrammar(2, 2))
