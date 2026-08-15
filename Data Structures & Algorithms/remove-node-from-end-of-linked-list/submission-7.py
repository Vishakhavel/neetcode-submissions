class Solution:
    def removeNthFromEnd(
        self,
        head: Optional[ListNode],
        n: int
    ) -> Optional[ListNode]:

        dummy = ListNode(0, head)

        # 1. Find the list length.
        length = 0
        current = head

        while current is not None:
            length += 1
            current = current.next

        # 2. Move to the node immediately before the target.
        previous = dummy

        for _ in range(length - n):
            previous = previous.next

        # 3. Unlink the target node.
        previous.next = previous.next.next

        return dummy.next