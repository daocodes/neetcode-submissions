class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dictionary = defaultdict(list)

        for s in strs:
            letters = [0] * 26
            for c in s:
                letters[ord(c) - 97] += 1


            dictionary[tuple(letters)].append(s)


        result = []

        for key, value in dictionary.items():
            sublist = []
            for v in value:
                sublist.append(v)

            result.append(sublist)


        return result
            

            


