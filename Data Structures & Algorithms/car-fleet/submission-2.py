class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        ps = []
        for i in range(len(position)):
            ps.append((position[i], speed[i]))
        
        # sort based on position O(NlogN)
        ps.sort()

        stack = []

        for i in range (len(ps) -1 , -1, -1):
            p, s = ps[i]
            curTime = (target - p)/s
            # if the time on the top of the stack is more than the current time required to reach the destination, don't add the curTime
            if(stack and stack[-1] >= curTime):
                continue
            else:
                stack.append(curTime)
        

        return len(stack)


