# Write a Python program to implement the concept of queue using list.
 
class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, item):
        self.queue.append(item)
    def dequeue(self):
        return None if self.size() < 1 else self.queue.pop(0)
    def size(self):
        return len(self.queue)
    def print_queue(self):
        print(self.queue)
 
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
print(f"Size of the queue: {q.size()}")
q.print_queue()
q.dequeue()
q.print_queue()