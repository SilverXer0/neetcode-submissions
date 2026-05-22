# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class NodeWrapper:
    def __init__(self, node):
        self.node = node

    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        dummy = ListNode()
        curr = dummy

        for temp in lists:
            if temp:
                heapq.heappush(heap, NodeWrapper(temp))

        while heap:
            wrapped_node = heapq.heappop(heap)
            node = wrapped_node.node
            curr.next = node

            if node.next:
                heapq.heappush(heap, NodeWrapper(node.next))

            curr = curr.next

        return dummy.next


        
            