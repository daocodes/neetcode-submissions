class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        
        

        pos_time = [0] * len(position)

        for i in range(len(position)):
            pos_time[i] = (position[i], (target - position[i]) / speed[i])

        pos_time.sort(reverse=True)
        if position:
            stack = [pos_time[0]]

        for i in range(1,len(position)):
            if pos_time[i][1] > stack[-1][1]:
                stack.append(pos_time[i])



        return len(stack)
        