from typing import Optional

from tree.treenode import TreeNode


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        l = []
        self.inorder(root, l)
        return l

    def inorder(self, root: Optional[TreeNode], l: list[int]):
        if root:
            self.inorder(root.left, l)
            l.append(root.val)
            self.inorder(root.right, l)
