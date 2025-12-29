
from typing import Optional


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        p = None
        q = head
        while q is not None:
            tmp = q.next
            q.next = p
            p = q
            q = tmp
        return p
