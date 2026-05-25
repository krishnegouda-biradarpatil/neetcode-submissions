class Solution:
    def scoreOfString(self, s: str) -> int:
        k=[]
        for i in s:
            k.append(ord(i))
        res=[]
        l=0
        for r in range(1,len(k)):
            res.append(abs(k[r]-k[l]))
            l=r
        return sum(res)