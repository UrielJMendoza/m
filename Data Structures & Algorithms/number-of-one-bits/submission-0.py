class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n >= 1:

            if n % 2 != 0:
                n = n // 2
                count +=1
            else:
                n = n / 2
            
        return count