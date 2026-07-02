class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo, hi = 1, max(piles)
        speed = hi

        while lo <= hi:
            mid = (lo + hi) // 2
            time = 0

            for pile in piles:
                time += math.ceil(float(pile) / mid)
            if time <= h:
                speed = mid
                hi = mid - 1
            else:
                lo = mid + 1

        return speed