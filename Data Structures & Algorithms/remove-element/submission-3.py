class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, j = 0, len(nums) - 1
        while j > 0 and nums[j] == val:
            j -= 1
        
        if j == 0: return 0
        
        while i < j:
            if nums[i] == val:
                nums[i], nums[j] = nums[j], nums[i]
                while nums[j] == val:
                    j -= 1
            i += 1

        return j+1
        