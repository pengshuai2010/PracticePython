from typing import Optional

from tree.treenode import TreeNode


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        values = set()

        # pre-order traversal
        def helper(root):
            if root is None:
                return False
            remainder = k - root.val
            if remainder in values:
                return True
            values.add(root.val)
            # Use "or" will short-curcuit the execution
            return helper(root.left) or helper(root.right)

if __name__ == '__main__':
    left = TreeNode(3, TreeNode(2), TreeNode(4))
    right = TreeNode(6, None, TreeNode(7))
    root = TreeNode(5, left, right)
    print(Solution().findTarget(root, 9))