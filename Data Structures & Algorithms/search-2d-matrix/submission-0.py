class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l=[]
        for i in matrix:
            l+=i
        left=0
        right=len(l)-1
        while left<=right:
            mid =left + ((right-left)//2)
            if l[mid]>target:
                right=mid-1
            elif l[mid]<target:
                left=mid+1
            else:
                return True
        return False

