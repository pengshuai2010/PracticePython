from typing import Optional

from tree.treenode import TreeNode


class Solution:
    # Divide and conquer. We return the result with a return type (easier in Python since we can use a tuple).
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        depth, diameter = self._helper(root)
        return diameter

    def _helper(self, root: Optional[TreeNode]) -> [int]:
        if root is None:
            return [0, 0]
        left_depth, left_diameter = self._helper(root.left)
        right_depth, right_diameter = self._helper(root.right)
        depth = 1 + max(left_depth, right_depth)
        diameter = max(left_diameter, right_diameter, left_depth + right_depth)
        return [depth, diameter]

# helper(self, root) -> depth, diameter

    # An alternative approach is traversal. We use post-order traversal to traverse the tree. The helper function
    # should return the depth of a node. And at each node update the global answer
    # self.max_depth = max(self.max_depth, left_depth + right_depth)
    def diameterOfBinaryTree_traversal(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def _helper(root: Optional[TreeNode]) -> int:
            if root is None:
                return 0
            # nonlocal tells the nested function that the variable lives in the nearest enclosing function scope
            nonlocal diameter
            left_depth = _helper(root.left)
            right_depth = _helper(root.right)
            depth = 1 + max(left_depth, right_depth)
            diameter = max(diameter, left_depth + right_depth)
            return depth

        _helper(root)
        return diameter