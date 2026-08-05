class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False



        setS = {}
        setT = {}

        for i in range(len(s)):
            setS[s[i]] = setS.get(s[i], 0) + 1
            setT[t[i]] = setT.get(t[i], 0) + 1




        return setS == setT
