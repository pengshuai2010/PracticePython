# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

from linkedlist.listnode import ListNode


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None:
            return
        fast, slow = self.split(head)
        other_head = slow.next
        slow.next = None
        other_head = self.reverse(other_head)
        return self.combine(head, other_head)

    def split(self, l):
        slow = l
        fast = l.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return [fast, slow]

    def reverse(self, l):
        p = None
        q = l
        while q:
            tmp = q.next
            q.next = p
            p = q
            q = tmp
        return p

    def combine(self, odd, even):
        dummy = ListNode()
        tail = dummy
        while odd or even:
            tail.next = odd
            tail = tail.next
            if odd:
                odd = odd.next
            tail.next = even
            tail = tail.next
            if even:
                even = even.next
        return dummy.next