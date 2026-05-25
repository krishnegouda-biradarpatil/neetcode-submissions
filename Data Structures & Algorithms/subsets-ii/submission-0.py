class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        res=set()
        sol=[]
        nums.sort()
        def backtrack(i):
            if i==n:
                res.add(tuple(sol[:]))
                return 
            
            #dont pick
            backtrack(i+1)
            #pick
            sol.append(nums[i])
            backtrack(i+1)
            sol.pop()
        backtrack(0)
        return [list(i) for i in res]