from typing import Optional

from tree.treenode import TreeNode


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        self._helper(root, val)
        return root

    def _helper(self, root: TreeNode, val: int):
        if root.val < val:
            if root.right:
                self._helper(root.right, val)
            else:
                root.right = TreeNode(val)
        else:
            if root.left:
                self._helper(root.left, val)
            else:
                root.left = TreeNode(val)

    # Time complexity is O(h) where h is the height of the tree. In the average case, O(h) = O(log(n)) where
    # is the size of the tree. In the worse case, O(h) = O(n). This happens when the tree is a degenerate tree.
    # If we build a BST in this way, and the input happens to be already sorted, we will get a degenerate tree
    # and worst performance.
    def insertIntoBST_simplified(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        else:
            root.left = self.insertIntoBST(root.left, val)
        return root
