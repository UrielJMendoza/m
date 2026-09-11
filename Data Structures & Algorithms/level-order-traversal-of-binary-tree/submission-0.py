# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        queue = deque()
        res = []
        
        if root:
            queue.append(root)
            #res.append([root.val])
            
        
        while len(queue) > 0:
            temp = []
            for i in range(len(queue)):
                
                
                curr =  queue.popleft()
                temp.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                   #temp.append(curr.left.val)
                  
                if curr.right:
                    queue.append(curr.right)
                    #temp.append(curr.right.val)
            res.append(temp)
                    
        return res
    
        