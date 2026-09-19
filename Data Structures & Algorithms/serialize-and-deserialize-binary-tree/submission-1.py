# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        ##use dfs and add into res if there is null or not and covert the values into string and call dfs left and right and then call dfs then return , join 
        def dfs(node):
            if not node:
                res.append("N")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(res)


        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        ##we go though vals and we split it by the delimter and we have a imcrementer i

        vals = data.split(",")
        self.i = 0
## we use dfs and check if the vals passed through is equal to null if so we inrecment i and return none
        def dfs():
            if vals[self.i] == "N":
                self.i += 1
                return None
            node = TreeNode(int(vals[self.i]))
            ##set the node == the value if not then increment i
            self.i +=1
            node.left = dfs()
            node.right = dfs()##then call dfs left and right
            return node ## return the tree 
        return dfs() ## return the return of dfs what is the tree
