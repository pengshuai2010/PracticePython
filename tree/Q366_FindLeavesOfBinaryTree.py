from typing import Optional, List

from tree.treenode import TreeNode


class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        # will root be null?
        if root is None:
            return []
        result = []

        # A dictionary is not necessary, because before a node at level (n + 1) is added, there must have been a node at level n added already
        # there will never be a case where level 1 is added but level 0 is not added.

        def helper(root: Optional[TreeNode]) -> int:
            if root is None:
                return -1
            left_level = helper(root.left)
            right_level = helper(root.right)
            level = max(left_level, right_level) + 1
            if len(result) - 1 < level:
                result.append([])
            result[level].append(root.val)
            return level

        helper(root)
        return result
