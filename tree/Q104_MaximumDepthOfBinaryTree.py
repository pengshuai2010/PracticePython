from typing import Optional
from collections import deque
from tree.treenode import TreeNode


class Solution:
    # Divide and Conquer: think about how to combine the results from left subtree and right subtree to get the the
    # result for the whole tree.
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    def __init__(self):
        self._max_depth = 0

    # Traversal. Traverse over the tree and update the result in class instance variable in the process.
    def maxDepth_traversal(self, root: Optional[TreeNode]) -> int:
        self._max_depth = 0
        self._traversal(root, 0)
        return self._max_depth

    def _traversal(self, root: Optional[TreeNode], depth: int):
        if root:
            self._max_depth = max(self._max_depth, depth + 1)
            self._traversal(root.left, depth + 1)
            self._traversal(root.right, depth + 1)

    # Level order traversal (BFS)
    def maxDepth_LevelOrderTraversal(self, root: Optional[TreeNode]) -> int:
        q = deque()
        depth = 0
        if root:
            q.append(root)
        while len(q) > 0:
            size = len(q)
            for i in range(size):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            depth += 1
        return depth

