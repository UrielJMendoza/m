class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        compare = {}
        for num in nums:
            if num not in compare:
                compare[num] = 1
            else:
                return True
        return False