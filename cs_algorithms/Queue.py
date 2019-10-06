
class Queue:

    def __init__(self):
        self.my_queue = []

    def enqueue(self, value):
        self.my_queue.append(value)

    def dequeue(self):
        if len(self.my_queue) == 0:
            "Underflow"
        else:
            value = self.my_queue[0]
            del(self.my_queue[0])
            return value

    def __repr__(self):
        return self.my_queue.__str__()
