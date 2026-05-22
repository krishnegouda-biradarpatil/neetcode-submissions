class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        r=0
        win_sum=0
        if sum(nums) < target:
            return 0

        count = float('inf')
        while r<len(nums):
            win_sum+=nums[r]
            while win_sum>=target:
                count=min(count,r-l+1)
                win_sum-=nums[l]
                l+=1
            r+=1
        return count

        

            



