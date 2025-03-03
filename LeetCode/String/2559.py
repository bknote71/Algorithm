class Solution:
    def vowelStrings(self, words: list[str], queries: list[list[int]]) -> List[int]:
        # 구간합
        vowels = "aeiou"
        n = len(words)
        cnt = [0] * (n + 1)
        for i in range(n):
            if words[i][0] in vowels and words[i][-1] in vowels:
                cnt[i] = 1

        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + cnt[i]  #  0..i 까지의 합

        answer = []

        for q in queries:
            s, e = q[0], q[1]
            answer.append(prefix[e + 1] - prefix[s])

        return answer
