class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d=defaultdict(int)
        res=max_c=0
        for i in nums:
            d[i]+=1
            if max_c<d[i]:
                res=i
                max_c=d[i]
        return res
        
