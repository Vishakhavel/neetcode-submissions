class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # implement binary search
        left, right = 0, len(nums) -1

        while(left <= right):
            index = (left + right)//2
            if(nums[index] > target):
                right-=1
            elif(nums[index] < target):
                left+=1
            else:
                return index
        
        return -1