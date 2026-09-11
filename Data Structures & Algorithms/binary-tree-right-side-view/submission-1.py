from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        res = []
        queue = deque()
        if root:
            queue.append(root)
        while len(queue) > 0:
            level_size = len(queue)
            for i in range(level_size):
                curr = queue.popleft()
                if i == level_size - 1:
                    res.append(curr.val)

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            
        return res