class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res=[]
        for i in range(len(arr)-1):
            max_e=max(arr[i+1:])
            res.append(max_e)
        res.append(-1)
        return res
            
