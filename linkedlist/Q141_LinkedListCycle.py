from typing import Optional

from linkedlist.listnode import ListNode


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        slow = head
        fast = slow.next
        while fast != slow:
            slow = slow.next
            if fast is None or fast.next is None:
                return False
            fast = fast.next.next
        return True
