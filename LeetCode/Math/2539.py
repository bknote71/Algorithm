from collections import Counter

# nCr을 페르마 소정리


class Solution:
    def countGoodSubsequences(self, s: str) -> int:
        count = Counter(s)
        mod = 10**9 + 7

        def mod_inv(x, mod):
            return pow(x, mod - 2, mod)  # 페르마의 소정리

        def precompute_factorials(n, mod):
            fact = [1] * (n + 1)
            inv_fact = [1] * (n + 1)

            for i in range(2, n + 1):
                fact[i] = (fact[i - 1] * i) % mod

            inv_fact[n] = mod_inv(fact[n], mod)
            for i in range(n - 1, 0, -1):
                inv_fact[i] = (inv_fact[i + 1] * (i + 1)) % mod

            return fact, inv_fact

        def combi(n, k, fact, inv_fact, mod):
            if k > n:
                return 0
            return (fact[n] * inv_fact[k] % mod) * inv_fact[n - k] % mod

        answer = 0

        n = max(list(count.values()))
        fact, inv_fact = precompute_factorials(n, mod)

        # nCk = (n-1)C(k-1) + (n-1)Ck
        # nC0, nC1 = 1

        for i in range(1, n + 1):
            cand = 1
            for k, v in count.items():
                if v >= i:
                    cand = (cand * (combi(v, i, fact, inv_fact, mod) + 1)) % mod

            answer = (answer + cand - 1) % mod

        return answer


print(Solution().countGoodSubsequences("aabb"))
