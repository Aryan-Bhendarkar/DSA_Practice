class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for i in operations:
            if i == "D":
                stack.append(int(stack[-1]*2))
            elif i == "C":
                stack.pop()
            elif i == "+":
                a = int(stack[-1])
                b = int(stack[-2])              
                stack.append(a+b)
            else:
                stack.append(int(i))

        sum = 0
        for i in stack:
            sum += i


        return sum
