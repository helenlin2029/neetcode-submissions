class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # the smallest eating speed is 1 (cannot be 0 otherwise it would never end)
        # the largest eating speed is gauranteed to be max(piles) because h must be greater 
        # the length of the list. If koko eats at the speed of the greatest value in the list,
        # the number of hours it will take is simply the length of the list. Therefore, it is 
        # logical that any eating speed faster than the maximum value will work. however, we are 
        # searching for if any value smaller will also result in an eating time less than h.
        lo, hi = 1, max(piles)
        # we set the current speed to be equal to the gauranteed value. if we find a valid speed 
        # slower than this, we can update speed.
        speed = hi

        #we are now closing the gap between the value we are testing and the value that is 
        # gauranteed. 
        while lo <= hi:
            # binary search is performed on EATING SPEED
            mid = (lo + hi) // 2
            time = 0

            # we start at the middle, calculating the total eating time if koko were to eat at
            # that speed.
            for pile in piles:
                time += math.ceil(float(pile) / mid)
            # if the time it takes is less than or equal to h, we know that koko is able to eat
            # slower and still finish within h. we therefore update speed and lower the boundary
            # for which koko is able to eat.
            if time <= h:
                speed = mid
                hi = mid - 1
            # if the time is not less than k, we know that koko has failed the task and must 
            # eat faster. therefore, we close the gap on the left side.
            else:
                lo = mid + 1

        return speed