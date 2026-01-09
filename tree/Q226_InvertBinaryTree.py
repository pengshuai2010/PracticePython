from typing import Optional

from tree.treenode import TreeNode


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is not None:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
