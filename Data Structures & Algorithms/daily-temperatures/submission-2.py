class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []


        res = [0] * len(temperatures)

        for curIndex, curTemp in enumerate(temperatures):
            while(stack and stack[-1][0] < curTemp):
                temp, index = stack.pop()
                res[index] = curIndex - index
            stack.append([curTemp, curIndex])
        
        return res
