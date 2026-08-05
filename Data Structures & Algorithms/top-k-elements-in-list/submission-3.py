class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary = {}

        freq = []

        for n in nums:
            freq.append([])


        for num in nums:
            dictionary[num] = dictionary.get(num, 0) + 1

        for key, value in dictionary.items():
            freq[value - 1].append(key)


        result = []
        
        
        for i in range(len(freq) -1 , -1, -1):
            for num in freq[i]:
                result.append(num)

                if len(result) == k:
                    return result



        
