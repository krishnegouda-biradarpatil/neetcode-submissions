class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        d={}
        max_f=0
        res=0
        for r in range(len(s)):
            d[s[r]]=d.get(s[r],0)+1
            max_f=max(max_f,d[s[r]])

            while (r-l+1)-max_f>k:
                d[s[l]] -=1
                l+=1
            res=max(res,r-l+1)
            
        return res


        

