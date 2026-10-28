# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = ListNode(0)
        dummy.next = head

        p2 = dummy
        for _ in range(n):
            p2 = p2.next
        
        p1 = dummy
        while p2.next:
            p1 = p1.next
            p2 = p2.next

        p1.next = p1.next.next
        return dummy.next