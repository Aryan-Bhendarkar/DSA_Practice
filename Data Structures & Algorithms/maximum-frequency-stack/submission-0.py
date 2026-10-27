class FreqStack:
    def __init__(self):
        self.map = defaultdict(int)
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.map[val] += 1

    def pop(self) -> int:
        maxcnt = max(self.map.values())
        i = len(self.stack) - 1
        while self.map[self.stack[i]] != maxcnt:
            i -= 1
        self.map[self.stack[i]] -= 1
        return self.stack.pop(i)
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()