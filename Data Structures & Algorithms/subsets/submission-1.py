class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets, curSet = [], []
        self.helper(0, nums, curSet, subsets)
        return subsets



    def helper(self, i, nums, curSet, subsets):
        if i >= len(nums):
            subsets.append(curSet.copy())
            return

        # decision to include nums[i]
        curSet.append(nums[i])
        self.helper(i + 1, nums, curSet, subsets)
        curSet.pop()

        # decision NOT to include nums[i]
        self.helper(i + 1, nums, curSet, subsets)