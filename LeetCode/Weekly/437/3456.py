class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        n = len(s)

        for i in range(n - k + 1):
            flag = True
            for j in range(k):
                if s[i] != s[i + j]:
                    flag = False
                    break

            if i > 0 and s[i] == s[i - 1]:
                flag = False
            if i < n - k and s[i] == s[i + k]:
                flag = False
            
            if flag == True:
                return True
                
        return False
