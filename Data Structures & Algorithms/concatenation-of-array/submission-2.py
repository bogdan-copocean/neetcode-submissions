class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * 2 * n
        i = 0
        while i < len(ans):
            ans[i] = nums[i%n]
            i += 1
        return ans