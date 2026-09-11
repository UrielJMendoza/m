# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0
        k = self.dfs(root)
        return self.max_diameter
        



    def dfs(self, root):
        if not root:
            return 0

        leftHeight = self.dfs(root.left)
        rightHeight = self.dfs(root.right)


        self.max_diameter = max(self.max_diameter,leftHeight+rightHeight)

        return 1 + max(leftHeight, rightHeight)

        