from typing import Optional

from tree.treenode import TreeNode


class Solution:
    # Divide and conquer.
    # Time complexity is O(M*N) where M and N are the sizes of the two trees.
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Clarify: Could subRoot be an empty tree?
        # Assuming subRoot is not None.
        if root is None:
            return False
        if self._is_same_tree(root, subRoot):
            return True
        if self.isSubtree(root.left, subRoot):
            return True
        if self.isSubtree(root.right, subRoot):
            return True
        return False

    def _is_same_tree(self, rootA: Optional[TreeNode], rootB: Optional[TreeNode]):
        if rootA is None and rootB is None:
            return True
        if rootA is None or rootB is None:
            return False
        return rootA.val == rootB.val and self._is_same_tree(rootA.left, rootB.left) and self._is_same_tree(rootA.right, rootB.right)

    # Alternative solution
    # First serialize the two trees using the same traversal order, e.g. preorder. Then check if the latter is a
    # substring of the former.
    # Serialization takes O(M + N) time. String matching takes O(M + N) time if we use an efficient string matching
    # algorithm like KMP or Z-algorithm.