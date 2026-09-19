import heapq
##we given pairs of xy and we want to 
## idk what k does but we wanna find what pair of xy is closet to the orgin 
## we have the distace calculated function here and so i think we run through each pair o xy and change the max but we check if they are eual first the handle duplicates and we add the xy pairs into a new array and return
## is the number amount of pair we wanna return

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []

        for x, y in points:
            distance = -(x**2 + y**2)
            heapq.heappush(maxHeap,[distance, x , y])
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
        res = []
        while maxHeap:
            distance , x , y = heapq.heappop(maxHeap)
            res.append([x,y])
        return res