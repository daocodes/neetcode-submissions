class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        
        for t in tokens:

            match t:
                
                case '+':
                    val1, val2 = int(stack.pop()), int(stack.pop())
                    stack.append(val1 + val2)
                case '-':
                    val1, val2 = int(stack.pop()), int(stack.pop())
                    stack.append(val2 - val1)
                case '/':
                    val1, val2 = int(stack.pop()), int(stack.pop())
                    stack.append(int(val2 / val1))
                case '*':
                    val1, val2 = int(stack.pop()), int(stack.pop())
                    stack.append(val1 * val2)
                case _:
                    stack.append(t)


        return int(stack[0])

                

            

