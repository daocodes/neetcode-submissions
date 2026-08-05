class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        post = 1
        pre = 1

        for i, n in enumerate(nums):
            result[i] = pre
            pre *=n

        
        for i in range(len(nums) -1, -1, -1):
            curr = nums[i]
            result[i] = result[i] *post

            post *= curr


        return result

