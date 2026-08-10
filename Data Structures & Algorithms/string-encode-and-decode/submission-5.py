class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedStr = ""
        for i in range(len(strs)):
            encodedStr += str(len(strs[i])) + "/" + strs[i]

        return encodedStr
        
    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0
        while i < len(s):
            slash = s.find("/", i)
            length = int(s[i:slash])
            ans.append(s[slash + 1 : slash + 1 + length])
            i = slash + 1 + length
        return ans