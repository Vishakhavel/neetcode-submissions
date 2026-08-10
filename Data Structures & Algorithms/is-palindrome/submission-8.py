class Solution:
    def isPalindrome(self, s: str) -> bool:
        start, end = 0, len(s) -1
        while(start < end):
            if(not self.isAlphaNum(s[start])):
                start+=1
                continue;

            if(not self.isAlphaNum(s[end])):
                end-=1
                continue;
            
            if(s[start].lower() != s[end].lower()):
                return False

            end-=1
            start+=1

        return True
    
    def isAlphaNum(self, c:str) -> bool:
        return(
            ord ('A') <= ord(c) <= ord('Z') or 
            ord ('a') <= ord(c) <= ord('z') or 
            ord ('0') <= ord(c) <= ord('9')
            )