class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        

        '''
        Input: piles is a list where each element is how many banans there are in a pile

        h = hours to eat the bananas
        Output: we need to return k which is the slowest rate in which we can eat all of the bananas

        '''
        largest = max(piles)

        
        

        l = 1
        r = largest
        





        while l <= r:
            m = (l + r) // 2

            
            currHours = 0
            for p in piles:
                currHours += math.ceil(float(p) / m)

            if currHours <= h:
                lowestK = m
                r = m - 1
            else:
                l = m + 1
        return lowestK





            
