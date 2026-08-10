class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create the value:frequency counter
        frequencies = Counter(nums)

        # create a heap
        heap = []

        for value, frequency in frequencies.items():
            heapq.heappush(heap, (frequency, value))

            if len(heap) > k:
                heapq.heappop(heap)

        
        ans = []
        for i in range(k):
            # get the value, frequency item from the heap array
            freq, value = heap[i]
            ans.append(value)
        
        return ans