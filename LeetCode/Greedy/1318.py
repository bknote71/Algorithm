class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        # 0번비트부터 31번비트까지 반복한다.
        bitmaks = 1
        answer = 0

        for i in range(32):
            amask = 1 if (a & bitmaks) > 0 else 0
            bmask = 1 if (b & bitmaks) > 0 else 0
            cmask = 1 if (c & bitmaks) > 0 else 0

            if amask | bmask != cmask:
                if cmask == 1:
                    answer += 1
                else:
                    answer += amask + bmask

            bitmaks <<= 1

        return answer


print(Solution().minFlips(8, 3, 5))
