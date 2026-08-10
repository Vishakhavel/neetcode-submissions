class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if(len(nums) == 0):
            return 0
        max_len = 1
        hashset = set()

        # create the hash set
        # O(N) time
        # O(N) space
        for i in nums:
            hashset.add(i)


        for i in nums:
            if(i-1 in hashset):
                continue
            else:
                cur = i
                l = 1
                while(cur+1 in hashset):
                    cur+=1
                    l+=1
                
                max_len=max(max_len, l)
        
        return max_len