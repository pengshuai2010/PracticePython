from collections import deque
from typing import Optional

from tree.treenode import TreeNode


class Solution:
    def __init__(self):
        self._result = 0

    def goodNodes(self, root: TreeNode) -> int:
        self._result = 0
        self._dfs(root, None)
        return self._result

    def _dfs(self, root: TreeNode, max_value: Optional[int]):
        if root is None:
            return
        if max_value == None or root.val >= max_value:
            self._result += 1
            max_value = root.val
        self._dfs(root.left, max_value)
        self._dfs(root.right, max_value)