class Solution:
    def climbStairs(self, n: int) -> int:
        if(n==0) or n ==1:
            total = 1
        else:
            t1 = 0
            t2 = 1

            for i in range(2, n+2):
                total = t1 + t2
                t1 = t2
                t2 = total
            
        return total