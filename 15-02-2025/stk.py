class Stack:
    def __init__(self) -> None:
        self.stack = []

    def size(self):
        return len(self.stack)

    def push(self, x):
        self.stack.append(x)
        print(x, "is added to the stack")

    def pop(self):
        try:
            return self.stack.pop()
        except IndexError as e:
            print(e)

    def __str__(self) -> str:
        return " ".join(map(str, self.stack))
