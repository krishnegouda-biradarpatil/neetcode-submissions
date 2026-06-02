class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
    
        
        cur_max=-1
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                if s[i]==s[j]:
                    cur_max=max(cur_max,j-i-1)
        return cur_max


        
                
            
