# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        curr = slow.next
        slow.next = None
        temp = curr
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        curr = head
        temp1 = curr
        temp2 = prev
        while prev:
            temp1 = curr.next
            curr.next = prev
            curr = temp1
            temp2 = prev.next
            prev.next = curr
            prev = temp2

        
        
        
            