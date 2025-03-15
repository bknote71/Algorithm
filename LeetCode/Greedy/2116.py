class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        # (, ) 요소 카운팅

        n = len(s)
        if n & 1 == 1:
            return False

        open_count = 0
        flex_count = 0

        for i in range(n):
            if locked[i] == "1":
                if s[i] == "(":
                    open_count += 1
                else:
                    open_count -= 1
            else:
                flex_count += 1
            if open_count + flex_count < 0:
                return False

        close_count = 0
        flex_count = 0

        for i in range(n - 1, -1, -1):
            if locked[i] == "1":
                if s[i] == ")":
                    close_count += 1
                else:
                    close_count -= 1
            else:
                flex_count += 1
            if close_count + flex_count < 0:
                return False

        return True


print(Solution().canBeValid("()))))", "111100"))
