class Solution:
    def encode(self, strs: List[str]) -> str:
        encode_str = ""
        for s in strs:
            encode_str += str(len(s))+"#"+s
        return encode_str

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j+1
            j = i+length
            strs.append(s[i:j])
            i=j

        return strs
