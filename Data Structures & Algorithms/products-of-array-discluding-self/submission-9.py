class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        total = 1
        containsZero = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                total *= nums[i]
            else:
                containsZero += 1

        for i in range(len(nums)):
            if containsZero == 0:
                result.append(total // nums[i])
            if containsZero == 1:
                if nums[i] == 0:
                    result.append(total)
                else:
                    result.append(0)
            if containsZero > 1:
                result.append(0)

        return result
