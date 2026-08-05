class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        answer = defaultdict(list)

        for s in strs:

            array = [0] * 26

            for l in s:
                
                array[ord(l) - ord('a')] += 1




            answer[tuple(array)].append(s)



        return list(answer.values())



        