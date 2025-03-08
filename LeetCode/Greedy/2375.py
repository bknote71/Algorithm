# DI string 문제


class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)
        arr = [str(i) for i in range(1, n + 2)]

        dstart = -1

        # [lo, hi] 뒤집기
        def reverse(lo, hi):
            print(f"reverse: {lo}, {hi}")
            while lo < hi:
                arr[lo], arr[hi] = arr[hi], arr[lo]
                lo += 1
                hi -= 1

            return

        for i, char in enumerate(pattern):
            if char == "D" and dstart == -1:
                dstart = i
            elif char == "I" and dstart != -1:
                reverse(dstart, i)
                dstart = -1

        if dstart != -1:
            reverse(dstart, n)

        return "".join(arr)


# print(Solution().smallestNumber("IIIDIDDD"))
print(Solution().smallestNumber("DDD"))
