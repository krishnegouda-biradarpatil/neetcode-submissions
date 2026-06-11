class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        c5=0
        c10=0
        for i in range(len(bills)):
            if bills[i]==5:
                c5+=1
            elif bills[i]==10:
                c5,c10=c5-1,c10+1
            elif c10>0:
                c5-=1
                c10-=1
            else:
                c5-=3
            if c5<0:
                return False
        return True