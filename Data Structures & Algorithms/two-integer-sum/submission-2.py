class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idxs = {}

        for i in range(len(nums)):
            idxs[nums[i]] = i

        for i in range(len(nums)):
            remaining = target - nums[i]
            if remaining in idxs.keys() and idxs[remaining] != i:
                if i < idxs[remaining]:
                    return [i, idxs[remaining]]
                else:
                    return [idxs[remaining], i]

        