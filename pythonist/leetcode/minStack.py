class MinStack:

    def __init__(self):
        self.stack = []
        self.stack_min = []

    def push(self, val):
        self.stack.append(val)
        if self.stack_min:
            val = min(val, self.stack_min[-1])
        self.stack_min.append(val)

    def pop(self):
        self.stack_min.pop()
        self.stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.stack_min[-1]


def main():
    pass



if __name__ == "__main__":
    main()
