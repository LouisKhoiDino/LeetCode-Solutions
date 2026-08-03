class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        from functools import lru_cache

        @lru_cache(None)
        def f(i, j):

            if j == len(p):
                return i == len(s)


            match = i < len(s) and (s[i] == p[j] or p[j] == '.')


            if j + 1 < len(p) and p[j + 1] == '*':
                return (
                    f(i, j + 2) or
                    (match and f(i + 1, j))
                )


            return match and f(i + 1, j + 1)

        return f(0, 0)