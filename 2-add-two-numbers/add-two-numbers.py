# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        ret = ListNode()
        curr = ret
        carryOver = 0

        while (l1 or l2 or carryOver):
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            value = x + y + carryOver
            carryOver = value // 10

            curr.next = ListNode(value % 10)
            curr = curr.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return ret.next