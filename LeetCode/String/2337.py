class Solution:
    def canChange(self, start: str, target: str) -> bool:
        # start to target
        # 어쨌든 순서는 정해져 있다.

        st = []
        ta = []
        n = len(start)

        for i in range(n):
            schar, tchar = start[i], target[i]
            if schar != "_":
                st.append((schar, i))

            if tchar != "_":
                ta.append((tchar, i))

        if len(st) != len(ta):
            return False

        n = len(st)

        for i in range(n):
            schar, si = st[i]
            tchar, ti = ta[i]
            if schar != tchar:
                return False

            if schar == "L" and si < ti:
                return False
            if tchar == "R" and si > ti:
                return False

        return True
