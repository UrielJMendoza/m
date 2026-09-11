class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        ###we want to vlidate the tree so we make a helper function that return the values of what it returns
        return self.dfs(root, float('-inf'), float('inf'))

##this is used with dfs given root with min and max vals
        
    
    def dfs(self, root, min_val, max_val):
        ### basic dfs structure we have base case if not root we return true becuase that means if nothing is there its valid it cant be non valid
        if not root:
            return True
        ## then we have the check to determine if the tree is valid so we say if its not that the min valu is less then the root value and the max value is greater than the root value
        ## then we return false

        if not (min_val < root.val < max_val):
            return False
        ##we check left and right and we have the new root become the left side and the min value 

        ## so we make for the left side we make root = root.left min val stays same and max val = root.val making sure its less that the root value
        left = self.dfs(root.left, min_val, root.val)

        ### makes sure its greater than the root value max val stays same
        right = self.dfs(root.right, root.val, max_val)

        return left and right