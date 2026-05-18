class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l=0
        res=len(nums)
        r=len(nums)-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]<target:
                l=mid+1
            elif nums[mid]>target:
                res=mid
                r=mid-1
            else:
                return mid
        return res


