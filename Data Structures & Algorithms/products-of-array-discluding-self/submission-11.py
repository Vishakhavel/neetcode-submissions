class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # note the number of 0s
        # track the product of all the numbers in the array

        # 1 0 implies => every element in the result array is zero, except the element at 0's index alone
        # 2 0s implies => every element in the result array is zero.
        # no zeroes means every element in the result array is product/that element

        zeroCount = 0
        prod = 1
        for i in nums:
            if i==0:
                zeroCount+=1
            else:
                prod*=i
        
        res = []
        print(zeroCount, prod)

        if(zeroCount == 0):
            for i in nums:
                res.append(prod//i)
            return res
        elif(zeroCount ==1):
            for i in nums:
                if(i == 0):
                    res.append(prod)
                else:
                    res.append(0)
            
            return res
        else:
            return [0] * len(nums)
        
