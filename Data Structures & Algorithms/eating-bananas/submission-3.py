class Solution:
    def eating_speed(self,piles,speed):
        total_h=0
        for i in piles:
            total_h+=math.ceil(i/speed)
        return total_h
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles)==h:
            return max(piles)
        m=max(piles)
        l=1
        r=m
        ans=0
        while l<=r:
            mid=(l+r)//2
            total_hour=self.eating_speed(piles,mid)
            if total_hour<=h:
                ans=mid
                r=mid-1
            else:
                l=mid+1
        return ans

        

            

            

        
        