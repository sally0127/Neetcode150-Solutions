class MinStack:

    def __init__(self):
        self.stack = []  # 主堆疊
        self.Minstack = []   # 最小值堆疊
        
    def push(self, val: int) -> None:
        # 將元素推入主堆疊
        self.stack.append(val)
        # 如果最小值堆疊為空，或者當前元素小於等於最小值堆疊的頂部，則推入最小值堆疊
        if not self.Minstack or val <= self.Minstack[-1]:
            self.Minstack.append(val)
        
    def pop(self) -> None:
        # 從主堆疊彈出頂部元素
        top = self.stack.pop()
        # 如果這個元素也是最小值堆疊的頂部，則同步從最小值堆疊彈出
        if top == self.Minstack[-1]:
            self.Minstack.pop()
       
    def top(self) -> int:
        # 返回主堆疊的頂部元素
        return self.stack[-1]

    def getMin(self) -> int:
        # 返回最小值堆疊的頂部元素，也就是當前最小值
        return self.Minstack[-1]
