class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_1=0
        cur=0
        for i in nums:
            
            if i==1:
                cur+=1
                max_1=max(max_1,cur)
            else:
                cur=0
        return max_1

            