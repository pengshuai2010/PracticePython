# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional, List

from tree.treenode import TreeNode


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        l = []
        self.preorder(root, l)
        return l

    def preorder(self, root, l):
        if root is not None:
            l.append(root.val)
            self.preorder(root.left, l)
            self.preorder(root.right, l)

    def preorderTraversal_iterative(self, root: Optional[TreeNode]) -> List[int]:
        l = []
        p = root
        stack = []
        while p or stack:
            # Why not use while p here? Because we would have to check validity of p and stack twice
            if p:
                l.append(p.val)
                if p.right:
                    stack.append(p.right)
                p = p.left
            else:
                p = stack.pop()
        return l