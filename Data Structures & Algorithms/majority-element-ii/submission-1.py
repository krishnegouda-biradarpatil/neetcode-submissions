class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d=defaultdict(int)
        k=len(nums)/3
        
        for i in nums:
            d[i]+=1
        res=[]
        for key ,val in d.items():
            if val>k:
                res.append(key)
        return res