class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len=0
        l=0
        charset=set()
        for i in range(len(s)):
            while s[i] in charset:
                
            
                charset.remove(s[l])
                l+=1
            charset.add(s[i])
            max_len=max(len(charset),max_len)
        return max_len

        