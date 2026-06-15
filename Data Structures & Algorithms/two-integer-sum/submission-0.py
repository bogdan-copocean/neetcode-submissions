class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        c_map = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in c_map:
                return [c_map[complement], i]

            c_map[nums[i]] = i

        return []
            

                