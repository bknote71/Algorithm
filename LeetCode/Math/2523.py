# 아니 그냥 sort 하면 되는문제 아닌가요?


class Solution:
    def closestPrimes(self, left: int, right: int) -> list[int]:
        # 1. left, right 소수 모은다.
        # 2. (diff, num1)을 list에 모은다.
        # 3. 그 list를 정렬한다.(오름차순)
        # 4. 사이즈가 0이면 [-1, -1]을 반환한다.
        # 5. 아니라면 첫 번째 [num1, num1 + diff]를 반환한다.

        is_prime = [True] * (right + 1)
        is_prime[0] = is_prime[1] = False

        for i in range(2, int(right ** (1 / 2)) + 1):
            if is_prime[i]:
                # i의 배수로 진행
                for j in range(i * i, right + 1, i):
                    is_prime[j] = False

        primes = [i for i in range(left, right + 1) if is_prime[i]]

        min_diff = float("inf")
        res = [-1, -1]

        for i in range(1, len(primes)):
            diff = primes[i] - primes[i - 1]
            if diff < min_diff:
                min_diff = diff
                res = [primes[i - 1], primes[i]]

        return res
