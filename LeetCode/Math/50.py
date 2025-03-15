class Solution:
    def myPow(self, x: float, n: int) -> float:
        # 이거는 분할 정복

        if n < 0:
            x = 1 / x
            n *= -1

        k = self.myPow(x, n // 2)
        return k * k * (x if n & 1 else 1)
