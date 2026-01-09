from typing import Optional

from tree.treenode import TreeNode


class Solution:
    # Divide and conquer
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # will p or q or root be None?
        # Are p and q guaranteed to exist in the tree?
        # Do we compare same object or just compare the value? If comparing values, will there be duplicates in the tree?
        # Assuming just compare values and all values in the tree are unique. And p and q are not None.
        _, __, lca = self._helper(root, p, q)
        return lca

    def _helper(self, root: Optional[TreeNode], p: TreeNode, q: TreeNode) -> [bool, bool, Optional[TreeNode]]:
        if root is None:
            return [False, False, None]
        left_has_p, left_has_q, left_lca = self._helper(root.left, p, q)
        if left_lca:
            return [True, True, left_lca]
        right_has_p, right_has_q, right_lca = self._helper(root.right, p, q)
        if right_lca:
            return [True, True, right_lca]
        if root.val == p.val and (left_has_q or right_has_q) or root.val == q.val and (
                left_has_p or right_has_p) or left_has_p and right_has_q or left_has_q and right_has_p:
            return [True, True, root]
        has_p = left_has_p or right_has_p or root.val == p.val
        has_q = left_has_q or right_has_q or root.val == q.val
        return [has_p, has_q, None]