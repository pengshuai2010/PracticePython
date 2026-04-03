# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

from tree.treenode import TreeNode


class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        nodes = []

        def inorder(root: Optional[TreeNode]):
            if root is None:
                return
            inorder(root.left)
            nodes.append(root)
            inorder(root.right)

        inorder(root)

        def construct_bst(start, end):
            if start > end:
                return None
            if start == end:
                node = nodes[start]
                node.left = None
                node.right = None
                return node
            mid = (start + end) // 2
            root = nodes[mid]
            root.left = construct_bst(start, mid - 1)
            root.right = construct_bst(mid + 1, end)
            return root

        return construct_bst(0, len(nodes) - 1)
