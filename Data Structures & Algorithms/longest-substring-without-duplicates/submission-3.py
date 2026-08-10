class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        uniqueChars = set()
        maxLen = 0
        left, maxLen, right = 0, 0, 0
        while(right < len(s)):

            # current character will always be what right is pointing to
            curChar = s[right]

            if(curChar in uniqueChars):
                while(curChar in uniqueChars and left < right):
                    uniqueChars.remove(s[left])
                    left+=1

            # add whats in the right index to the set
            uniqueChars.add(s[right]);
            maxLen = max(maxLen, len(uniqueChars))
            right+=1
        

        return maxLen