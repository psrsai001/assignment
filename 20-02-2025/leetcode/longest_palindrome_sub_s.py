class Solution:
    def longestPalindrome(self, s: str) -> str:

        n = len(s)
        sub = (-1, -1)
        max_len = 0
        for i in range(n):
            # odd len sub string
            l = r = i
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 > max_len:
                    sub = (l, r)
                    max_len = r - l + 1
                l -= 1
                r += 1

            # even len sub string
            l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 > max_len:
                    sub = (l, r)
                    max_len = r - l + 1
                l -= 1
                r += 1
        return s[sub[0] : sub[1] + 1]
