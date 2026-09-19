class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        current = 0
        count = 0
        for i in range(len(nums)):
            if count == 0:
                current = nums[i]
                count +=1
                continue
            if current == nums[i]:
                count += 1
            if count >= 2:
                count = 0
                current = 0
            
        return current
    
            
        