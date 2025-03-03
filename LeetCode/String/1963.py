class Solution:
    def minSwaps(self, s: str) -> int:
        if not s:
            return 0

        # 최소 스왑 개수

        news = []
        for char in s:
            if char == "]" and news and news[-1] == "[":
                news.pop()
            else:
                news.append(char)

        return (len(news) // 2 + 1) // 2
