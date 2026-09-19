class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        largestk = max(piles)
        l = 1
        r = largestk
        lowest = largestk



        while l <= r:
            m = (l + r) // 2
            hours = 0

            for p in piles:
                hours += math.ceil(float(p) / m)

            if hours <= h:
                lowest = m
                r = m - 1

            else:
                l = m + 1

        return lowest
        