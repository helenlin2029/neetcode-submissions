class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        list = []
        for i in range(len(nums)):
            if nums[i] not in list:
                list.append(nums[i])
            else: 
                return True

        return False