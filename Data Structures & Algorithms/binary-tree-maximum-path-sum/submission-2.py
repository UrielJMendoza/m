class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float('-inf')

        ### we make a max sum variable with negative infi
##use dfs i was right on dfs algo and we make max sum non local to dfs so we can update it 

        def dfs(node):
            nonlocal max_sum
            if not node:
                return 0##we have our base case if not node then wereturn 0 bassicly
            ##call left and right dfs but get max of the dfs
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)
            ##then we store the max of the mac sum and the left plus right plus root
            max_sum = max(max_sum, node.val + left + right)
            #then we return it then max again until we get the max max
            return node.val + max(left, right)
##cal dfs and return max sum 
        dfs(root)
        return max_sum
        ##so we continusly update max untill we cant anymore