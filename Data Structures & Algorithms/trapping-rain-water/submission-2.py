class Solution:
    def trap(self, height: List[int]) -> int:


        if not height:
            ##base case if all empty return 0
            return 0
        l = 0 
        r = len(height) - 1
        leftMax = height[l]
        rightMax = height[r]
#then we make left and right pointers with leftmax and right max set and the end
##make res variable
        res = 0 
##clasic while l < r two pointer aproach
        while l < r:
            if leftMax < rightMax:
                ## if the left max is less than the right max then we move left one over and calc new left max and add to the res of the max left compred to the value in heigh
                l += 1
                leftMax = max(height[l], leftMax)
                res += leftMax - height[l]
# rightMax is taller, so leftMax is the limiting water level.
# Any space between height[l] and leftMax must be trapped water.
            else:
                ## else we move r down and compute right max
                ##then we add to res and return res
                r-= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res