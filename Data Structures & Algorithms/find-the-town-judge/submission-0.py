class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        income=defaultdict(int)
        out=defaultdict(int)
        for src,dest in trust:
            out[src]+=1
            income[dest]+=1
        for i in range(1,n+1):
            if out[i]==0 and income[i]==n-1:
                return i
        return -1