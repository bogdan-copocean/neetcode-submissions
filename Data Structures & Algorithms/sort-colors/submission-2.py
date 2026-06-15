class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 2 1 0
        # 1 2 0
        l, r = 0, len(nums) - 1
        i = 0
        while i <= r:
            if nums[i] == 0:
                nums[i], nums[l] = nums[l], nums[i]
                l += 1
            if nums[i] == 2:
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1
                i -= 1
            i += 1



