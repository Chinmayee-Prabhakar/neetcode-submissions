class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        sort_array = []
        for num, cnt in count.items():
            sort_array.append([cnt,num])

        sort_array.sort()

        result = []
        while len(result) < k:
            result.append(sort_array.pop()[1])
        
        return result

        