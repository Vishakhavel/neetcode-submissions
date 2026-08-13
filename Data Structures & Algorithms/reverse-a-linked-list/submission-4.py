# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(head is None):
            return None

        cur, prev, temp = head, None, None

        while(cur is not None):
            temp = cur.next
            cur.next = prev
            prev =cur
            cur = temp
        return prev