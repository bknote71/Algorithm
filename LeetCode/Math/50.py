class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        
        if n == 1:
            return x

        if n < 0:
            x = 1 / x
            n *= -1

        k = self.myPow(x, n // 2)
        return k * k * (x if n & 1 else 1)
