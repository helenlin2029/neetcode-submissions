class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}
        ans = []

        for num in nums:
            if num not in freqs:
                freqs[num] = 0
            freqs[num] += 1

        sort = dict(sorted(freqs.items(), key=lambda item: item[1]))

        for i in range(k):
            number, frequency = sort.popitem()
            ans.append(number)

        return ans

        

        
            
            