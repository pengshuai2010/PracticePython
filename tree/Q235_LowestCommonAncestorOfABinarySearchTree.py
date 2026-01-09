class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # will p or q or root be None?
        # Are p and q guaranteed to exist in the tree?
        # Do we compare same object or just compare the value? If comparing values, will there be duplicates in the tree?
        # Assuming just compare values and all values in the tree are unique. And p and q are not None.
        node = root
        while node:
            if p.val < node.val and q.val < node.val:
                node = node.left
            elif p.val > node.val and q.val > node.val:
                node = node.right
            else:
                return node
        raise ValueError()