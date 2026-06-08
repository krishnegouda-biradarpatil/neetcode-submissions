class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]
        
        def backtrack(i,cur):
            
            
            if i>n:
                if len(cur)==k:
                    res.append(cur[:])
                return 

            backtrack(i+1,cur)
            cur.append(i)
            backtrack(i+1,cur)
            cur.pop()
        backtrack(1,[])
        return res

        