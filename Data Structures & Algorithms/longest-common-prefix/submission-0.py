class Solution:
    def longestCommonPrefix(self, strs):
        prefix = strs[0]
        for s in strs[1:]:
            while s[:len(prefix)]!=prefix:
                prefix = prefix[:-1]  # shorten prefix
                if not prefix:
                    return ""
        return prefix
