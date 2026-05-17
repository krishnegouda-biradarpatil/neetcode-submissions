class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n=min(len(word1),len(word2))
        l=0
        s=""
        r=n-1
        for i in range(n):
            s+=word1[i]+word2[i]
        if len(word1)==n:
            s+=word2[n:]
        else:
            s+=word1[n:]
        return s

