class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)


        for i in range(len(temperatures)):
            
            while stack and stack[-1][0] < temperatures[i]:
                curr = stack.pop()
                result[curr[1]] = i - curr[1]

            stack.append(tuple((temperatures[i], i)))

        return result


        '''
        lowest is tracked,
        then pop when u get a higher value
        [30,38

        '''