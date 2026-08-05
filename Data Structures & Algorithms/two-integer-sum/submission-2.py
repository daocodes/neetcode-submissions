class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashMap = {}
        for i, n in enumerate(nums):

            if n in hashMap:
                answer = list()
                answer.append(hashMap[n])
                answer.append(i)
                return answer
            
            compliment = target - n
            hashMap[compliment] = i



            
        