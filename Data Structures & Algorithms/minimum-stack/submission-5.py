class MinStack:

    def __init__(self):
        self.stack = []
        self.minlist = []

    def push(self, val: int) -> None:
        if not self.minlist:
            self.minlist.append(val)
        else:
            if val < self.minlist[-1]:
               self.minlist.append(val)
            else:
                self.minlist.append(self.minlist[-1])
        self.stack.append(val)
        
    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.minlist.pop()


    def top(self) -> int:
        if not self.stack:
            return -1
        return self.stack[-1]
        

    def getMin(self) -> int:
        if not self.minlist:
            return -1
        else:
            return self.minlist[-1]
        
