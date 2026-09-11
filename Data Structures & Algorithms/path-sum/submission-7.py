# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    path = 0 
    diff = 0 

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        global path
        global dif



        if not root:
            return False
            ## so we check if there is root is not return false


        self.path += root.val
       ##add rootval to opath
            

        
        if not root.left and not root.right and root.val - targetSum == 0:
            return True
#winnng case if leaf node meaning no more down and root.val - target sym = 0 so diference meaning they are the same then return true that there is a path

        if self.hasPathSum(root.left,targetSum-root.val):
            self.path += root.val
            return True

##if path has left node then we go left and use target sum - root.val so decrementing target sum 

        if self.hasPathSum(root.right,targetSum-root.val):
            self.path += root.val
            return True
##same thing here 

        return False
        
##if we dont get anything out of the recursiive calls we end up at return false
        