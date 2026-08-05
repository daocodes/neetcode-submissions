class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        bucket = []
        seen = {}

        for i in range(len(nums)):
            bucket.append([])

        for n in nums:
            if n in seen:
                seen[n] = seen.get(n) + 1
            else:
                seen[n] = 1

        result = []
        for key, value in seen.items():
            bucket[value - 1].append(key)



        for b in range(len(nums) - 1, -1, -1):
            for val in bucket[b]:
                result.append(val)
                if len(result) == k:
                    return result
                




            