class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    # Check if queue is full
    def is_full(self):
        return (self.rear + 1) % self.size == self.front

    # Check if queue is empty
    def is_empty(self):
        return self.front == -1

    # Insert element into the queue
    def enqueue(self, value):
        if self.is_full():
            print("Queue is Full! Cannot insert", value)
            return
        if self.front == -1:  # First element
            self.front = 0
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = value
        print(f"Enqueued: {value}")

    # Remove element from the queue
    def dequeue(self):
        if self.is_empty():
            print("Queue is Empty! Cannot dequeue")
            return None
        value = self.queue[self.front]
        if self.front == self.rear:  # Queue becomes empty
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        print(f"Dequeued: {value}")
        return value

    # Display elements in the queue
    def display(self):
        if self.is_empty():
            print("Queue is Empty")
            return
        print("Queue elements:", end=" ")
        i = self.front
        while True:
            print(self.queue[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.size
        print()


# Example usage
if __name__ == "__main__":
    cq = CircularQueue(5)

    cq.enqueue(10)
    cq.enqueue(20)
    cq.enqueue(30)
    cq.enqueue(40)
    cq.enqueue(50)   # Queue full now
    cq.display()

    cq.dequeue()
    cq.dequeue()
    cq.dequeue()
    cq.display()

    cq.enqueue(60)
    cq.enqueue(70)
    cq.display()
