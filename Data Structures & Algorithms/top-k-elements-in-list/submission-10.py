class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        bucket = [[] for i in range(len(nums) + 1)]

        for num, cnt in count.items():
            bucket[cnt].append(num)

        result = []
        for i in range(len(bucket)-1, 0, -1):
            for n in bucket[i]:
                result.append(n)
                if len(result) == k:
                    return result

