class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=""
        
        for i in s:
            if i.isalnum():
                l=l+i.lower()
        left=0;right=len(l)-1
        
        k=""
        for i in range(len(l)-1,-1,-1):
            k=k+l[i]
        # return k
        return (True if k==l else False)

        # while left<right:
        #     l[left],l[right]=l[right],l[left]
        #     left+=1
        #     right-=1
        # return (True if l==k)

        