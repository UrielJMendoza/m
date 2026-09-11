# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
probably use dfs
run through nodes with a tracker varible of the root and hcekc if its greater add to list if not continue

"""


class Solution:

    def goodNodes(self, root: TreeNode) -> int:
        validNums = []
        k = self.dfs(root, -9999999)
        return k


    def dfs(self, root, max_so_far):
        count = 0
        if not root:
            return 0
        if root.val >= max_so_far:
            count += 1

        new_max = max(max_so_far, root.val)
        left = self.dfs(root.left, new_max)
        right = self.dfs(root.right, new_max)
        return count + left + right
