class MinStack:

    def __init__(self):
        self.item = []
        self.min_values = []
        

    def push(self, val: int) -> None:
        self.item.append(val)
        if self.min_values == []:
            self.min_values.append(val)
        else:
            min_item = min(self.min_values[-1], val)
            self.min_values.append(min_item)
        

    def pop(self) -> None:
        self.item.pop()
        self.min_values.pop()
        

    def top(self) -> int:
        return self.item[-1]
        

    def getMin(self) -> int:
        return self.min_values[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()