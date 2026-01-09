from typing import Optional

from tree.treenode import TreeNode


class Solution:
    # Divide and Conquer.
    # Time complexity is O(N) because in the worst case all tree nodes will be visited
    # Space complexity is O(N) in the worst case (degenerate binary tree), and O(log(N)) in the best case (balanced
    # binary tree).
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if p is None and q is not None or p is not None and q is None:
            return False
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
