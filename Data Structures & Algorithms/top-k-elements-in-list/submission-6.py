class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        heap = []
        for num, cnt in count.items():
            heapq.heappush(heap, (cnt,num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        result = []
        while len(result) < k:
            result.append(heap.pop()[1])

        return result
        