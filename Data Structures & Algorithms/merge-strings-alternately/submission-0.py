class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m = n = 0
        string = ""
        
        while m < len(word1) and n < len(word2):
            string = string + word1[m]
            m += 1
            string = string + word2[n]
            n += 1

        if m < len(word1):
            string += word1[m:]
        if n < len(word2):
            string += word2[n:]

        return string 