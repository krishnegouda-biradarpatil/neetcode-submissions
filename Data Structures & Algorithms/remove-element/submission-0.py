class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n=[]
        for i in range(len(nums)):
            if nums[i]!=val:
                n.append(nums[i])
            else:
                continue

        for i in range(len(n)):
            nums[i] = n[i]
        return len(n)
        
        