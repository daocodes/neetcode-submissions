class Solution:
    def isPalindrome(self, s: str) -> bool:


        def isAlpha(c):
            return ord('0') <= ord(c) <= ord('9') or ord('a')<= ord(c) <= ord('z') or ord('A')<= ord(c) <=ord('Z')


        l = 0
        r = len(s) - 1
        s = s.lower()

        while (l < r):
            if not isAlpha(s[l]):
                l = l + 1
            if not isAlpha(s[r]):
                r = r - 1
            while (l < r) and isAlpha(s[l]) and isAlpha(s[r]):
                if s[l] != s[r]:
                    return False
                l = l + 1
                r = r - 1
        return True


