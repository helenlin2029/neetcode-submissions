class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        nums = {}

        for i in range(len(numbers)):
            nums[numbers[i]] = i

        for i in range(len(numbers)):
            complement = target - numbers[i]
            if complement in nums and i != nums[complement]:
                if nums[complement] > i:
                    return [i + 1, nums[complement] + 1]