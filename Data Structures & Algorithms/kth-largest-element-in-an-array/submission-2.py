import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        ##we replace all them with negatives
        for i in range(len(nums)):
            nums[i] = -nums[i]
        heapq.heapify(nums)##then we add it all to a min heap and this sorts max for us

        ##while len (stones > 1)
        for i in range(k-1):##then we go thorugh kth eleemeths popping until done
            heapq.heappop(nums)
        return -heapq.heappop(nums) #then we return negative heappop nums for the greatest element to convert back to positive