from typing import Optional

from tree.treenode import TreeNode


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # guaranteed to be a valid BST? Is the size of tree guaranteed to be greater than or equal to k?
        # inorder traversal, get the kth node (1-indexed)
        count = 0
        p = root
        stack = []
        while p or stack:
            if p:
                stack.append(p)
                p = p.left
            else:
                p = stack.pop()
                # visit
                count += 1
                if count == k:
                    return p.val
                p = p.right
        raise ValueError()
