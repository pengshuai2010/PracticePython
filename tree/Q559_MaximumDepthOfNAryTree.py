"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0
        if root.children is None or len(root.children) == 0:
            return 1
        max_depth = 0
        for child in root.children:
            child_depth = self.maxDepth(child)
            max_depth = max(max_depth, child_depth)
        return max_depth + 1
