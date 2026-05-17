class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res=[]
        for i in nums:
            if i not in res:
                res.append(i)
        res.sort()
        cnt_max=1
        cnt=1
        l=0
        r=1
        while r<len(res):
            if res[r]-res[l]==1:
                cnt+=1
                l+=1
                r+=1
            else:
                cnt=1
                l+=1
                r+=1
            cnt_max=max(cnt_max,cnt)
        if len(nums)>0:
            return cnt_max
        else:
            return 0

                