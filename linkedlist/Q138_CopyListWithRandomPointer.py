"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # clarify random node will only point to None or a node in the list?
        if head is None:
            return None
        d = {}
        p = head
        while p:
            q = Node(p.val) # Is ListNode hashable?
            d[p] = q
            p = p.next
        p = head
        d[None] = None # avoids None check for p.next and p.random
        while p:
            q = d[p]
            q.next = d[p.next]
            q.random = d[p.random]
            p = p.next
        return d[head]