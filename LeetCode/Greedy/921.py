class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        for c in list(s):
            if c == ")" and stack and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(c)

        return len(stack)
