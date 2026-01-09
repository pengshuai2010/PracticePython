from typing import Optional, List
from treenode import TreeNode

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

    def inorderTraversal_interative(self, root: Optional[TreeNode]) -> List[int]:
        l = []
        stack = []
        p = root
        while p or stack:
            if p: # Why not use while p? Because we would have to check the validity of p and stack twice
                stack.append(p)
                p = p.left
            else:
                p = stack.pop()
                # visit
                l.append(p.val)
                p = p.right
        return l