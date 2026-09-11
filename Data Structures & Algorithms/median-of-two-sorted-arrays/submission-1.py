class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num3 = nums1 + nums2
        num3.sort()
        if len(num3) % 2 == 0:
            mid = len(num3) // 2

            
            s = (num3[mid - 1] + num3[mid]) / 2
            return s
        else:
            mid = len(num3) // 2
            return num3[mid]
        