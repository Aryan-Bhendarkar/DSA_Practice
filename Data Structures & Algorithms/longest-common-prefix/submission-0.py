class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_length = 201
        prefix = ""
        for str in strs:
            min_length = min(min_length, len(str))

        for i in range(min_length):
            curr = strs[0][i] 
            for str in strs:
                if str[i] != curr:
                    return prefix
            
            prefix += curr
        
        return prefix