class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre_p=[0]*len(nums)
        post_p=[0]*len(nums)
        count=0
        res=[0]*len(nums)
        prod=1
        
        for i in nums:
            if i==0:
                count+=1
            else:
                prod=prod*i
        
        for i in range(len(nums)):
            if count==0:
                res[i]=int(prod/nums[i])
            elif count==1 and nums[i]==0:
                res[i]=prod
            if count>=2:
                return res
        return res
            
                


        
            

            

        