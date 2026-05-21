class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        queue=[]
        
        while len(stones)>1:
            stones.sort()
            cur=abs(stones.pop()-stones.pop())
            if cur:
                stones.append(cur)
        return stones[0] if stones else 0
            