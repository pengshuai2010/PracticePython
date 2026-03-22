from typing import Optional

from tree.treenode import TreeNode


class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        # will root be empty?
        if not root:
            return -1
        minimum = root.val
        second_min = None

        def helper(root: Optional[TreeNode]):
            nonlocal second_min
            if not root:
                return
            if root.val == minimum:
                helper(root.left)
                helper(root.right)
            elif second_min is None or root.val < second_min:
                second_min = root.val
                # when root.val > minimum, we don't need to go down further because the values in the subtree
                # won't get any smaller

        helper(root)
        if second_min is None:
            return -1
        return second_min