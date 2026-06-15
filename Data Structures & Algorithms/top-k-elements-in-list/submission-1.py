class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        
        result = []
        for num, count in counts.items():
            heapq.heappush(result, (-count,num))

        returned = []
        for _ in range(k):
            tup = heapq.heappop(result)
            returned.append(tup[1])

        return returned