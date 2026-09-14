# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return None
##as with any dfs algo we have our base case since its recursions and if not root then return none 
        if root.val < p.val and root.val < q.val:
            ##then if we have both p and q values greater than root value
            ## we make a recurive call to the method then we move right one
            return self.lowestCommonAncestor(root.right, p, q)
        ##else we move the root to the left
        elif root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
##if none of those are true then we return the root since thats where they split
        else:
            return root