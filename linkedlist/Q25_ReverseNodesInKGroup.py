# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

from linkedlist.listnode import ListNode


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        slow = dummy
        fast = self._get_kth(slow, k)
        while fast:
            next_start = fast.next
            fast.next = None
            new_tail = slow.next
            new_head = self._reverse(slow.next)
            slow.next = new_head
            new_tail.next = next_start
            slow = new_tail
            fast = self._get_kth(slow, k)
        return dummy.next

    def _reverse(self, head):
        p = None
        q = head
        while q:
            tmp = q.next
            q.next = p
            p = q
            q = tmp
        return p

    def _get_kth(self, node, k):
        for i in range(k):
            if node:
                node = node.next
            else:
                break
        return node
