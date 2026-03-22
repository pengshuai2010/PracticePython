from typing import Optional

from tree.treenode import TreeNode


class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        if root.left is None and root.right is None:
            return root

        parent = self.upsideDownBinaryTree(root.left)
        new_root, new_left, new_right = root.left, root.right, root
        new_root.left = new_left
        new_root.right = new_right
        root.left = None
        root.right = None
        return parent

# helper(root):
#     if root is leaf node
#         return root
#     left = root.left
#     right = root.right
#     parent = helper(left)
#     new_root = left
#     new_left = right
#     new_right = root
#     new_root.left = new_left
#     new_root.right = new_right
#     return parent