class Solution:
    def maxSubstringLength(self, s: str, k: int) -> bool:
        if k == 0:
            return True
        
        n = len(s)
        if k > n:
            return False

        # 각 문자의 처음과 마지막 위치 저장
        left = {}  
        right = {}

        for i, char in enumerate(s):
            if char not in left:
                left[char] = i
            right[char] = i

        intervals = [(left[c], right[c]) for c in right.keys()]
        intervals.sort(key=lambda x: x[1])

        count = 0
        last = -1

        for start, end in intervals:
            if last < start:
                count += 1
                last = end

        print(k)

        return count >= k

print(Solution().maxSubstringLength("ddjlopbgngpoenkqktvuuvpygctyquoeqglszijjiifljfiswiladdfwzislzdd", 6))