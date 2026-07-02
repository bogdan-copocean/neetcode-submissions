class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        result = 0
        counter = 0
        for num in nums:
            counter = counter + 1 if num else 0
            result = max(result, counter)

        return result