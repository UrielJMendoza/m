import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        #so we have a heap and they are min heaps so we negate it to be the smallest big number
##areverse all stones in stones
        stones = [-s for s in stones]
        ##put it all into one heap
        heapq.heapify(stones)
        ##while len (stones > 1)
        while len(stones) > 1:
            ##make varibale first and second with poping off the top
            ##if they are equal they will never get added back on since diference owuld be 0 maybe
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            ##if they are not equal then we add the diference of first minus second
            if first != second:
                heapq.heappush(stones, first - second)
        if len(stones) == 0:
            return 0
        return -stones[0]