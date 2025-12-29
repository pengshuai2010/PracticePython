# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

from linkedlist.listnode import ListNode


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Could any of the input be empty? If empty, can I return the other ?
        # do I have to create a copy? modify the input OK?
        dummy = ListNode()
        tail = dummy
        p = l1
        q = l2
        carry = 0
        while p or q or carry > 0:
            total = carry
            if p:
                total += p.val
                p = p.next
            if q:
                total += q.val
                q = q.next
            carry = total // 10
            value = total % 10
            node = ListNode(value)
            tail.next = node
            tail = tail.next
        return dummy.next