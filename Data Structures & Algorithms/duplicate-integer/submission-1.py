class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count_map ={}
        for i in nums:
            if i in count_map:
                count_map[i]+=1
                if count_map[i]>1:
                    return True 
            else:
                count_map[i]=1
        return False