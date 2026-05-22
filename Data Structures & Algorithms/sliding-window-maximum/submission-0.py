class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l=0
        win=nums[l:k]
        res=[]
        win_max=max(win)
        for r in range(k,len(nums)+1):
            res.append(max(nums[l:r]))
            l+=1
        return res