from __future__ import annotations

from typing import Optional, Tuple

from tree.treenode import TreeNode


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None

        def helper(node) -> Tuple[bool, bool, TreeNode | None]:
            if node is None:
                return False, False, None

            left_has_p, left_has_q, left_lca = helper(node.left)
            if left_lca is not None:
                return True, True, left_lca

            right_has_p, right_has_q, right_lca = helper(node.right)
            if right_lca is not None:
                return True, True, right_lca

            if left_has_p and right_has_q or left_has_q and right_has_p:
                return True, True, node

            if node == p and (left_has_q or right_has_q) or node == q and (left_has_p or right_has_p):
                return True, True, node

            has_p = left_has_p or right_has_p or node == p
            has_q = left_has_q or right_has_q or node == q
            lca = None
            return has_p, has_q, lca

        _, _, lca = helper(root)
        return lca