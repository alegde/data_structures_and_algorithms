
class Stack:

    def __init__(self):
        self.my_stack = []

    def _is_empty(self):
        if len(self.my_stack) == 0:
            return True
        else:
            return False

    def push(self, value):
        self.my_stack.append(value)

    def pop(self):
        if self._is_empty():
            return "Underflow"
        else:
            a = self.my_stack[-1]
            del(self.my_stack[-1])
            return a

    def __repr__(self):
        return self.my_stack.__str__()
