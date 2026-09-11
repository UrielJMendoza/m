class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0

        for right in range(len(nums)):
            if nums[right] == nums[left]:
                continue
            else:
                nums[left+1] = nums[right]
                left +=1
                

        return left + 1
        
        