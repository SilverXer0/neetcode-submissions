# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        curr = head
        length = 1
        while curr.next:
            curr = curr.next
            length += 1

        curr = dummy
        t = length - n
        x = 0
        while x < t:
            curr = curr.next
            x += 1
        curr.next = curr.next.next

        return dummy.next
