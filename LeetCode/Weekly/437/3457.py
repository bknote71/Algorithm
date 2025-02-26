class Solution:
    def maxWeight(self, pizzas: list[int]) -> int:
        # 정렬 후 n / 4 횟수로 더할 수 있음

        n = len(pizzas)
        k = n // 4  
        
        even = k // 2 # even-numbered 횟수
        odd = k - even

        s = n - 1
        answer = 0

        pizzas.sort()

        for i in range(odd):
            answer += pizzas[s]
            s -= 1
        
        s -= 1

        for i in range(even):
            answer += pizzas[s]
            s -= 2

        return answer

print(Solution().maxWeight([5,2,2,4,3,3,1,3,2,5,4,2]))