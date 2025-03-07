class Queue:
    def __init__(self):
        self.queue = []
    def add(self,name):
        self.queue.append(name)
    def next(self):
        if len(self.queue) == 1:
            raise ValueError("You only have one item in the queue")
        return self.queue.pop(0)
queue = Queue()

# Add item to queue instance
queue.add("Pablo")
queue.next()
# Print queue contents
print(queue.queue)
    