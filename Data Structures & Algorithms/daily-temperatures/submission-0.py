class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, current_temp in enumerate(temperatures):
            while stack and current_temp > stack[-1][0]:
                stackT, stackI = stack.pop()
                res[stackI] = i - stackI

            stack.append((current_temp, i))
        
        return res
