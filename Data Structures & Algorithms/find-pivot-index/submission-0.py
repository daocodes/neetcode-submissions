class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        s = sum(nums)
        currentSum = 0
        for i in range(len(nums)):
            s -= nums[i]
            if s - currentSum == 0:
                return i

            currentSum += nums[i]
            

        return -1


        
