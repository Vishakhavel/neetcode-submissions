# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # carry overs all the way.

        carryover = False
        node1, node2 = l1, l2

        res = ListNode(0)
        temp = res

        while node1 is not None and node2 is not None:
            sum = node1.val + node2.val

            if carryover:
                sum += 1
                carryover = False

            if sum > 9:
                sum -= 10
                carryover = True
            
            temp.next = ListNode(sum)
            temp = temp.next
            node1=node1.next
            node2=node2.next
        

        # check if node1 is None and continue for node2, or the other way round

        if(node1 is None):
            while(node2 is not None):
                sum = node2.val
                if(carryover):
                    sum+=1
                    carryover = False

                if(sum > 9):
                    sum-=10
                    carryover = True

                temp.next = ListNode(sum)
                temp = temp.next
                node2 = node2.next
            

        elif(node2 is None):
            while(node1 is not None):
                sum = node1.val
                if(carryover):
                    sum+=1
                    carryover = False

                if(sum > 9):
                    sum-=10
                    carryover = True

                temp.next = ListNode(sum)
                temp = temp.next
                node1 = node1.next
            
        # if there is still a carry over, add 1 to the last digit
        if(carryover):
            temp.next = ListNode(1)
            temp = temp.next

        return res.next
        