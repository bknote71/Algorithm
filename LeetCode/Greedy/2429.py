class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        # num2의 최상위 비트 이후의 비트(in num1) + num2
        cnt = 0
        while num2 > 0:
            cnt += 1 if num2 & 1 else 0
            num2 >>= 1

        onebits = []
        zerobits = []

        for i in range(32):
            if num1 & (1 << i):
                onebits.append(i)
            else:
                zerobits.append(i)

        n = len(onebits)
        zeroidx = 0
        answer = 0

        for i in range(cnt):
            if n - 1 - i >= 0:
                answer += 1 << onebits[n - 1 - i]
            else:
                answer += 1 << zerobits[zeroidx]
                zeroidx += 1

        return answer


print(Solution().minimizeXor(3, 5))
