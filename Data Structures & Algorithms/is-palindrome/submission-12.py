class Solution:
    def isPalindrome(self, s: str) -> bool:
        

        def isAlpha(letter):
            if ord('a') <= ord(letter) <= ord('z') or ord('A') <= ord(letter) <= ord('Z') or ord('0') <= ord(letter) <= ord('9'):
                return True

            else:
                return False

        l = 0
        r = len(s) -1
        
        while l < r:

            while l < r and not isAlpha(s[l]):
                l+=1

            while l < r and not isAlpha(s[r]):
                r-=1

            if (l < r) and s[r].lower() != s[l].lower():
                return False

            l+=1
            r-=1
        
        return True

