class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashs = {}


        for i in range(len(nums)):


            dif = target - nums[i]


            if dif in hashs:
                return [hashs[dif], i]


            hashs[nums[i]] = i

                    
