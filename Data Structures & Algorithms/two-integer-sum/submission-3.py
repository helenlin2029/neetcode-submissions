class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idxs = {}

        for i, n in enumerate(nums):
            idxs[n] = i

        for i in range(len(nums)):
            remaining = target - nums[i]
            if remaining in idxs and idxs[remaining] != i:
                if i < idxs[remaining]:
                    return [i, idxs[remaining]]
                else:
                    return [idxs[remaining], i]

        