from typing import Optional

from tree.treenode import TreeNode


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        # Can I include reference to part of the original tree? Or do I have to have create a new copy?
        if root1 is None:
            return root2
        if root2 is None:
            return root1
        root = TreeNode(root1.val + root2.val)
        left = self.mergeTrees(root1.left, root2.left)
        right = self.mergeTrees(root1.right, root2.right)
        root.left = left
        root.right = right
        return root