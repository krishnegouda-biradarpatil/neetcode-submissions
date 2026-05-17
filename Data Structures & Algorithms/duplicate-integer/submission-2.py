class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d=defaultdict(int)
        for i in nums:
            d[i]+=1
        for key,val in d.items():
            if val>1:
                return True
        return False
    

        
        