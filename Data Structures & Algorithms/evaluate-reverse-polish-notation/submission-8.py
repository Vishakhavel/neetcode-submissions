class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if(token in ['*', '+', '-', '/']):
                # get the right and left operands
                right = stack.pop()
                left = stack.pop()

                # evaluate the value
                result = self.calculate(right, left, token)
                stack.append(result)
            else:
                stack.append(int(token))
        
        return stack.pop()

    def calculate(self, r, l, operation) -> int:
        if(operation == '*'):
            return r*l
        elif(operation == '-'):
            return l-r
        elif(operation == '+'):
            return l+r
        else:
            return int(l/r)
