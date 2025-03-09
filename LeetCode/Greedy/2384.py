from collections import defaultdict


class Solution:
    def largestPalindromic(self, num: str) -> str:
        # num을 char to count 딕셔너리로 쪼갠다.
        # char.values()가 큰 순서대로 (즉 9부터 하면 될 듯)

        # 1. value = 2 * even + odd 형태
        # - odd는 가운데에 두고 더 이상의 odd는 만들지 않는다.
        # - even 개수만큼 앞 뒤에 붙인다.

        chars = defaultdict(int)
        for char in num:
            chars[int(char)] += 1

        odd_num = -1
        answer = ""

        for i in range(9, -1, -1):
            even, odd = chars[i] // 2, 1 if chars[i] & 1 else 0

            if odd > 0 and odd_num == -1:
                odd_num = i

            if even > 0:
                if i == 0 and not answer:
                    break

                for _ in range(even):
                    answer = answer + str(i)

        answer = answer[:] + (str(odd_num) if odd_num != -1 else "") + answer[::-1]

        return answer if answer else "0"


# print(Solution().largestPalindromic("00"))
# print(Solution().largestPalindromic("444947137"))
