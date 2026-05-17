class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left=0
        n=len(numbers)
        right=n-1
        res=[]
        while left<right:
            cur_sum=numbers[left]+numbers[right]
            if cur_sum>target:
                right-=1
            elif cur_sum<target:
                left+=1
            else:
                return [left+1,right+1]
        return []
            
                # left+=1
        
            

        