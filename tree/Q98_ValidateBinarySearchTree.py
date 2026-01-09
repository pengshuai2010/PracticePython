from typing import Optional

from tree.treenode import TreeNode


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # in-order traversal and make sure the traversal is in ascending order
        # or divided and conquer. max value from left subtree should be less than root value, min value from right subtree should
        # be greater than root value.
        if root is None:
            return True
        last_value = float('-inf')
        p = root
        stack = []
        while p is not None or len(stack) > 0:
            if p:
                stack.append(p)
                p = p.left
            else:
                p = stack.pop()
                # visit
                if p.val <= last_value:
                    return False
                last_value = p.val
                p = p.right
        return True