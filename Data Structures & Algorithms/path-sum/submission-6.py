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


        self.path += root.val
       
            

        
        if not root.left and not root.right and root.val - targetSum == 0:
            return True


        if self.hasPathSum(root.left,targetSum-root.val):
            self.path += root.val
            return True



        if self.hasPathSum(root.right,targetSum-root.val):
            self.path += root.val
            return True

        return False
        

        