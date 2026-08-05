class Solution:
    def isValid(self, s: str) -> bool:
        

        correct = {'}':'{', ']':'[', ')': '('}

        stack = []



        for c in s:
            if c in correct:
                    
                if stack and stack[-1] == correct[c]:
                    stack.pop()

                else:
                    return False


            



            else:
                stack.append(c)


        return True if not stack else False
                
