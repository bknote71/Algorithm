from collections import defaultdict


class Solution:
    def decodeString(self, s: str) -> str:
        # 1. 쌍을 매핑한다. open to close
        opentoclose = defaultdict(int)
        stack = []
        for i, char in enumerate(s):
            if char == "[":
                stack.append(i)
            elif char == "]":
                opentoclose[stack.pop()] = i

        # [lo, hi)
        def solve(lo, hi) -> str:
            i = lo
            curnum = 0
            answer = ""

            while i < hi:
                char = s[i]

                if char.isdigit():
                    curnum = 10 * curnum + int(char)
                elif char.isalpha():
                    answer += char
                elif char == "[":
                    answer += solve(i + 1, opentoclose[i]) * curnum
                    curnum = 0
                    i = opentoclose[i]
                    # continue

                i += 1

            print(lo, hi, answer)

            return answer

        return solve(0, len(s))


print(Solution().decodeString("3[a]2[bc]"))
