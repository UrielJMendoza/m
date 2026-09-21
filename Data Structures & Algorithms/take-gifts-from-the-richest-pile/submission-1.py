import heapq
import math
#we want to create a max heap and pop the max into a varible then 
##nwe have to add sqrt of value int var 
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        ## 
    
        


        gifts = [-g for g in gifts]
        heapq.heapify(gifts)

        for i in range(k):
            biggest = -heapq.heappop(gifts)
            
            result = math.floor(sqrt(biggest))
            heapq.heappush(gifts, -result)
            

        return -sum(gifts)
            
        

        