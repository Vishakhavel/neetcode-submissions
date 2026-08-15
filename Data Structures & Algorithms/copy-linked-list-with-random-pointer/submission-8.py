"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # 1. CREATE a map of the existing -> duplicate node

        temp = head
        map = {}
        while(temp is not None):
            map[temp] = Node(temp.val)
            temp = temp.next
            # just copy the values and create a new list node

        

        # now one more loop through the dict and link the nexts and the randoms.

        for old, new in map.items():
            new.random = map.get(old.random) or None
            new.next = map.get(old.next) or None
        

        return map.get(head)