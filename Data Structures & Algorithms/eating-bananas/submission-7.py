class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # binary search between 1 and the max element in the array that satisfies the condition.

        # binary search between 1 and max of the piles.
        left, right = 1, max(piles)


        while(left <= right):
            cur = (left+right)//2
            hours = 0
            # see if the condition is satisfied.
            for pile in piles:
                hours+=math.ceil(pile/cur)

            if(hours > h):
                left=cur+1
            
            elif(hours <= h):
                right=cur-1


        return left