class Stack:
    def __init__(self):
        self.stack = []
        self.min_num_stack = []

    def push(self, element):
        self.stack.append(element)
        if not self.min_num_stack or element < self.min_num_stack[-1]:
            self.min_num_stack.append(element)

    def pop(self):
        res = self.stack.pop()
        if res == self.self.min_num_stack[-1]:
            self.min_num_stack.pop()
        return res

    def top(self):
        return self.stack[-1]

    def get_min(self):
        return self.self.min_num_stack[-1]