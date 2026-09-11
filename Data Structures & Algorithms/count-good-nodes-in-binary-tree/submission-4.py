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

##so we want to use dfs to caclaute the length to the root and if the value is greater than the length to the root then its alid and we want to return the numbers of numbs that are valid
class Solution:

    def goodNodes(self, root: TreeNode) -> int:
        ### so we  call and store our dfs call with root and a very small number
        k = self.dfs(root, -9999999)
        return k # then we return self.dfs 


    def dfs(self, root, max_so_far):

        #create a dfs method and create a count varibale

        count = 0

        ##make the standard dfs algo if not root return 0
        if not root:
            return 0
            #then we check the root values if its greater than the max seen so far and thats -9999 so true

        if root.val >= max_so_far:
            count += 1# we increment count

        new_max = max(max_so_far, root.val)
        ##we make a new max and it starts to what every the root value is 

        left = self.dfs(root.left, new_max)
        ## call left and right dfs with the new max recursivly
        right = self.dfs(root.right, new_max)

        ## after we calculte the length from the root then compare it to the current value we increment count and then recursivly call dfs left and rigth until done and return count + left + right becuase it also stores count we want total valid numbers
        return count + left + right
