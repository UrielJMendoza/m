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
        ##call recursion dfs


    def dfs(self,root, k):
        #base case
        if not root:
            return 
        
        

        #recursion case
        
        left = self.dfs(root.left,k)
        #check left dfs
        #if left is it then we return left
        if left is not None:
            return left
        ##increment the count of dfs times so we can track k vs count
        self.count += 1
        
        if self.count == k:##if count == k then we have to return the value we are on with the root values
            return root.val
        

        ##if not all those then call and check right dfs 

        right = self.dfs(root.right,k)
        ## then we check if its right and return right is so
        if right is not None:
            return right
        
        
        