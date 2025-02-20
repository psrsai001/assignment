class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        st = ""
        n1 = len(word1)
        n2 = len(word2)
        min_st = min(n1, n2)

        for i in range(min_st):
            st += word1[i]
            st += word2[i]
        if n1 == min_st:
            return st + word2[n1:]
        return st + word1[n2:]
