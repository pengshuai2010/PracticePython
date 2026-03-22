from collections import deque
from typing import Optional

from tree.treenode import TreeNode


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        # assuming the tree is not empty
        # assuming k <= size of the tree
        queue = deque()

        def inorder(root: Optional[TreeNode]):
            stack = []
            node = root
            while stack or node:
                while node:
                    stack.append(node)
                    node = node.left
                # visit
                node = stack.pop()
                queue.append(node.val)
                if len(queue) > k:
                    head = queue[0]
                    tail = queue[-1]
                    if abs(head - target) > abs(tail - target):
                        queue.popleft()
                    else:
                        queue.pop()
                        # An optimization:
                        # The newly added element is further away. The rest of the element will only be even
                        # further away.
                        break
                node = node.right

        inorder(root)
        return list(queue)



    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        # assuming the tree is not empty
        # assuming k <= size of the tree

        queue = deque()

        # The potential problem with recursion: if the binary tree is a degenerate binary tree, i.e. it
        # too imbalanced, the depth will be O(n), so the recursion depth becomes O(n), which can lead to
        # stack overflow.
        def inorder(root: Optional[TreeNode]):
            if not root:
                return
            inorder(root.left)
            queue.append(root.val)
            if len(queue) > k:
                head = queue[0]
                tail = queue[-1]
                if abs(head - target) > abs(tail - target):
                    queue.popleft()
                else:
                    queue.pop()
            inorder(root.right)

        inorder(root)
        return list(queue)