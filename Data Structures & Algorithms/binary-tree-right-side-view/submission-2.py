from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        res = []
        queue = deque()

        ##make res for results importt deque for bfs


        if root:
            queue.append(root)
#check if the root is there then add into qeue

        while len(queue) > 0:
            level_size = len(queue)

            ##while len qeue greater than 0 then we have the qeue size strod in level size
            # then we go through the level with the for loop
            for i in range(level_size):
                curr = queue.popleft()
                ## curr = the left pop val 
                ## if i in the for loop is equal to the level sieze minus one meaning the most right element
                if i == level_size - 1:
                    res.append(curr.val)# then we append it to our results array

                if curr.left: # basic bfs search child nodes left andf right and append them into the qeue
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            # finally after qeue is empy and we added all the right msot elements we return res
        return res