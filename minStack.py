class MinStack:

    def __init__(self):
        self.minstack = []
        

    def push(self, val: int) -> None:
        if self.minstack:
            minm = self.minstack[-1][1]
            if minm > val:
                self.minstack.append([val, val])
            else:
                self.minstack.append([val, minm])
        else:
            self.minstack.append([val, val])

    def pop(self) -> None:
        if self.minstack:
            return self.minstack.pop()[0]

    def top(self) -> int:
        if self.minstack:
            return self.minstack[-1][0]

    def getMin(self) -> int:
        if self.minstack:
            return self.minstack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()