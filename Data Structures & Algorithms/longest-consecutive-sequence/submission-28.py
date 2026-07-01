class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        count = 0

        for num in numbers:
            if (num - 1) not in numbers:
                length = 1
                while (num + length) in numbers:
                    length += 1
                count = max(length, count)
            
        return count
            

            