class Solution:
    def isValid(self, s: str) -> bool:
        matching = {"}": "{", "]": "[", ")": "("}
        stack = []

        for char in s:
            if(char in '({['):
                stack.append(char)
            else:
                if(len(stack) == 0 or stack[-1] != matching[char]):
                    return False
                
                stack.pop()
        
        return len(stack) == 0