class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = defaultdict(int)
        idx = defaultdict(int)
        for num in nums:
            counts[num] += 1

        mx = -1
        res = nums[0]
        for val, cnt in counts.items():
            if cnt > mx:
                res = val
                mx = cnt

        return res