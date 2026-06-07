class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        l=0
        people=sorted(people)
        r=len(people)-1
        count=0
        while l<=r:
            if l < r and people[l]+people[r] <= limit:
                l+=1
                r-=1
            else:
                r-=1
            count+=1
        return count