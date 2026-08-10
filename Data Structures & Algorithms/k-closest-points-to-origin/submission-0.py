class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []

        # iterate through all the points.
        for x,y in points:
            # push a tuple into the minHeap array -> (distance, x , y)
            heapq.heappush(minHeap, (-self.getDistance(x,y), x, y))

        
        # now pop until we have the k closest points
        while(len(minHeap) > k):
            heapq.heappop(minHeap)
        

        return [[x, y] for distance, x, y in minHeap]

    def getDistance(self, x:int, y:int):
        return math.sqrt(x*x + y*y)