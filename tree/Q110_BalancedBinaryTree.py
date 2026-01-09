from typing import Optional

from tree.treenode import TreeNode


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        _, is_balanced = self._helper(root)
        return is_balanced

    # Divide and conquer.
    def _helper(self, root: Optional[TreeNode]) -> [int, bool]:
        if root is None:
            return [0, True]
        left_height, left_balanced = self._helper(root.left)
        # The optimization doesn't change the big-O time complexity though
        # The time complexity would still be O(N) where N is the number of nodes in the tree.
        if not left_balanced:
            return [0, False]
        right_height, right_balanced = self._helper(root.right)
        if not right_balanced:
            return [0, False]
        height = max(left_height, right_height) + 1
        is_balanced = abs(left_height - right_height) <= 1
        return [height, is_balanced]

    def _helper(self, root: Optional[TreeNode]) -> [int, bool]:
        if root is None:
            return [0, True]
        left_height, left_balanced = self._helper(root.left)
        right_height, right_balanced = self._helper(root.right)
        height = max(left_height, right_height) + 1
        is_balanced = abs(left_height - right_height) <= 1 and left_balanced and right_balanced
        return [height, is_balanced]