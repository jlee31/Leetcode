# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head

        while cur:
            tmp = cur.next # save the next node
            cur.next = prev # set it backwards
            prev = cur # we set the backwards, now we move up once
            cur = tmp # set current to what we saved as next
        
        return prev
