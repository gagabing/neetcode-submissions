class MinStack:

    def __init__(self):
        self.stack = []
        self.smallest = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.smallest.append(val)
        self.smallest.sort()

    def pop(self) -> None:
        p = self.stack.pop()

        for elem in self.smallest:
            if elem == p:
                self.smallest.remove(p)
                break
        return p
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.smallest[0]
        
