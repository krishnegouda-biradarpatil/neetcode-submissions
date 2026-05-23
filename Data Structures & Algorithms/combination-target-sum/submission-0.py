class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        n=len(nums)
        def backtrack(i,cur,total):
            if total==target:
                res.append(cur[:])
                return 
            if i>=n or total>target:
                return 
            
            #dont pick nums[i]
            backtrack(i+1,cur,total)
            #pick nums[i]
            cur.append(nums[i])
            backtrack(i,cur,total+nums[i])
            cur.pop()
        backtrack(0,[],0)
        return res

            