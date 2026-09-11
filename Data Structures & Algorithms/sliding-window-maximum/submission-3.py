from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not k:
            return []
        
        MaxElements = []
    
        left = 0 
        window = deque([])

        for right in range(len(nums)):
            while window and nums[window[-1]] <= nums[right]:
                window.pop()
            window.append(right)

            if window[0] < right - k + 1:
                window.popleft()

            if right >= k - 1:
                MaxElements.append(nums[window[0]])

        return MaxElements