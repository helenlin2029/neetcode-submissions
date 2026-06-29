class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        shown = set()
        for i in range(len(nums)):
            if nums[i] in shown:
                return True
            shown.add(nums[i])

        return False