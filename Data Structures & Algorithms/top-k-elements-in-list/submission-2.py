class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        
        result = []
        for num, count in counts.items():
            heapq.heappush(result, (count,num))
            if len(result) > k:
                heapq.heappop(result)

        returned = []
        for _ in range(k):
            returned.append(heapq.heappop(result)[1])

        return returned