class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # s = "jar", t = "jam"

        count1, count2 = {}, {}

        for index, char in enumerate(s):
            count1[char] = count1.get(char, 0) +1;

            #count1 = {"j":1, "a":1, "r":1}

        for index, char in enumerate(t):
            count2[char] = count2.get(char, 0) +1;
            #count2 = {"j":1, "a":1, "m":1}
        
        # now verify that both these count dicts have equivalent values

        # if length of dicts are diff, return false
        if(len(count1) != len(count2)):
            return False

        # if the lengths are equal, loop the dict
        for char in count1.keys():
            if(char not in count2):
                return False
            elif(count2[char] != count1[char]):
                return False
        

        # after you've looped through everything, return True

        return True