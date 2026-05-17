class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        n=len(heights)
        r=n-1
        max_h=0
        while l<r:
            res=(r-l)*min(heights[r],heights[l])
            max_h=max(max_h,res)
            if heights[l]<=heights[r]:
                l+=1
            else:
                r-=1

            
            
            
        return max_h
        