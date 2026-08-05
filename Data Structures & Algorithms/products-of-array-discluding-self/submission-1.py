class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftSum = 1
        rightSum = 1
        result = [1] * len(nums)

        index = 0


        for i in range(1, len(nums) ):
            leftSum *= nums[index]
            rightSum *= nums[len(nums)-1 - index]

            index += 1

            result[i] *= leftSum
            result[len(nums) -1 - i] *= rightSum

        return result




















