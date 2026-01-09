from typing import List, Optional

from tree.treenode import TreeNode


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None
        root = TreeNode(preorder[0])
        mid = inorder.index(root.val) # mid is also the size of the left subtree
        root.left = self.buildTree(preorder[1: 1 + mid], inorder[:mid])
        root.right = self.buildTree(preorder[1 + mid:], inorder[mid + 1:])
        return root

    def buildTree_preorderTraversal(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None
        pre_index = 0

        def dfs(l, r):  # inorder traversal dfs
            if l >= r:
                return None
            nonlocal pre_index
            root = TreeNode(preorder[pre_index])
            pre_index += 1

            mid = inorder.index(root.val)
            root.left = dfs(l, mid)
            root.right = dfs(mid + 1, r)
            return root

        return dfs(0, len(preorder))