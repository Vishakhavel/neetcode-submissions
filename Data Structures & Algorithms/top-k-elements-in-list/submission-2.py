class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = Counter(nums)
        heap = []

        for value, frequency in frequencies.items():
            heapq.heappush(heap, (frequency, value))

            if len(heap) > k:
                heapq.heappop(heap)

        return [value for frequency, value in heap]
        