from typing import Optional

from tree.treenode import TreeNode


class Solution:

    def goodNodes(self, root: TreeNode) -> int:
        result = 0

        def _dfs(root: TreeNode, max_value: Optional[int]):
            # Indicates that result is not a local variable but instead a variable from the immediately enclosing
            # function.
            nonlocal result
            if root is None:
                return
            if max_value is None or root.val >= max_value:
                result += 1
                max_value = root.val
            _dfs(root.left, max_value)
            _dfs(root.right, max_value)

        _dfs(root, None)
        return result