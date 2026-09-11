class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root, float('-inf'), float('inf'))
    
    def dfs(self, root, min_val, max_val):
        if not root:
            return True
        
        if not (min_val < root.val < max_val):
            return False
        
        left = self.dfs(root.left, min_val, root.val)
        right = self.dfs(root.right, root.val, max_val)

        return left and right