# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

from linkedlist.listnode import ListNode


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # is there guarantee that n > 0, length of list >= n?
        if head is None:
            return None
        fast = head
        for i in range(n):
            fast = fast.next
        dummy = ListNode()
        dummy.next = head
        slow = dummy
        while fast:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy.next


# test cases
# empty list
# len < n
# [1], n = 2 guaranteed not happen.
# [1], n = 1
# [1, 2], n = 2