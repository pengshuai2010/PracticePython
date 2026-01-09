import heapq
from typing import List, Optional

from linkedlist.listnode import ListNode


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        min_heap = [Wrapper(node) for node in lists if node is not None]
        heapq.heapify(min_heap)
        while len(min_heap) > 0:
            wrapper = heapq.heappop(min_heap)
            node = wrapper.node
            tail.next = node
            tail = tail.next
            if node.next is not None:
                next_node = node.next
                heapq.heappush(min_heap, Wrapper(next_node))
        return dummy.next

# why a wrapper class is needed? Because ListNode doesn't implement __lt__ method, and we don't have the
# access to modify it.
class Wrapper:
    def __init__(self, node: ListNode):
        self.node = node

    def __lt__(self, other):
        return self.node.val < other.node.val
