class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        res=len(blocks)
        for i in range(len(blocks)-k+1):
            cnt_w=0
            for j in range(i,i+k):
                if blocks[j]=="W":
                    cnt_w+=1
            res=min(res,cnt_w)
        return res
