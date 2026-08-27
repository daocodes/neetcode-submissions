class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        result = []
        #sorted array = [-4, -1, -1, 0, 1, 2]

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            
            l = i + 1
            r = len(nums) - 1

            while l < r:
                curr = nums[i] + nums[l] + nums[r]

                if curr < 0:
                    l+=1

                elif curr > 0:
                    r-=1

                else:
                    if [nums[i], nums[l], nums[r]] not in result:
                        result.append([nums[i], nums[l], nums[r]])
                    r-=1
                    l+=1

        return result




                


            



        
