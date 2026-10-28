# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr = head
        while curr and curr.next and curr.next.next:
            # find the second-to-last node
            prev = curr
            while prev.next.next:
                prev = prev.next
            last = prev.next
            prev.next = None          # detach the tail
            last.next = curr.next     # splice it in after curr
            curr.next = last
            curr = last.next          # move two steps forward

            