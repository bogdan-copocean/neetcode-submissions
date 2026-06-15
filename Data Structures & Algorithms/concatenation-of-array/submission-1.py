class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * 2 * n
        i = 0
        for i, num in enumerate(nums):
            ans[i+n] = num
            ans[i] = num
        return ans