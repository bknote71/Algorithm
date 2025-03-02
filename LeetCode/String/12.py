class Solution:
    def intToRoman(self, num: int) -> str:
        answer = ""

        maps = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I"),
        ]

        for value, symbol in maps:
            if num == 0:
                break

            count, num = divmod(num, value)
            answer += symbol * (count)

        return answer


print(Solution().intToRoman(3749))
