class MyQueue(object):

    def __init__(self):
        self.stack = []
        self.end = 0
        self.first = 0

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        print(self.stack)
        

    def pop(self):
        """
        :rtype: int
        """
        return self.stack.pop(0)
        

    def peek(self):
        """
        :rtype: int
        """
        
        return self.stack[0]
        

    def empty(self):
        """
        :rtype: bool
        """
        
        if self.stack:
            return False
        return True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()