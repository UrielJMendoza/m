# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        ##global count variable

        return self.dfs(root, k)


    def dfs(self,root, k):
        #base case
        if not root:
            return 
        
        

        #recursion case
        
        left = self.dfs(root.left,k)
        if left is not None:
            return left
        self.count += 1
        
        if self.count == k:
            return root.val
        

        
        right = self.dfs(root.right,k)
        if right is not None:
            return right
        
        
        