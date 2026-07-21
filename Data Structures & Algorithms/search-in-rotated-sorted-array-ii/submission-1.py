class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l=0
        r=len(nums)-1
        for i in nums:
            if i==target:
                return True
        return False
