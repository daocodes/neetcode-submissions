class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        tracker = set(nums)
        longest = 0


        for n in nums:

            if (n-1) not in tracker:
                current = 0

                while (current + n) in tracker:
                    current +=1

                if current > longest:
                    longest = current

        return longest


