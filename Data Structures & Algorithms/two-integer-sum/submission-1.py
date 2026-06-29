class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idxs = {}

        for i in range(len(nums)):
            idxs[i] = nums[i]

        for i in range(len(nums)):
            remaining = target - nums[i]
            if remaining in idxs.values() and nums.index(remaining) != i:
                if i < nums.index(remaining):
                    return [i, nums.index(remaining)]
                else:
                    return [nums.index(remaining), i]

        