from typing import Optional, List

from tree.treenode import TreeNode
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []
        curr_level = []
        if root:
            curr_level.append(root)
        while len(curr_level) > 0:
            next_level = []
            for node in curr_level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            levels.append([item.val for item in curr_level])
            curr_level = next_level
        return levels

    def levelOrder_deque(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []
        q = deque()
        if root:
            q.append(root)
        while len(q) > 0:
            size = len(q)
            curr_level = []
            for i in range(size):
                node = q.popleft()
                curr_level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            levels.append(curr_level)
        return levels