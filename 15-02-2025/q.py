from ll_node import LinkedList


class Queue:
    def __init__(self):
        self.q = []

    def size(self):
        return len(self.q)

    def enqueue(self, x):
        self.q.append(x)
        print("enqueued:", x)

    def dequeue(self):
        try:
            x = self.q.pop(0)
            print("Dequeued:", x)
            return x
        except IndexError as e:
            print(e)

    def __str__(self):
        return " ".join(map(str, self.q))


class QueueLL:
    def __init__(self):
        self.q = LinkedList()

    def size(self):
        return self.q.size()

    def enqueue(self, x):
        self.q.insert_end(x)
        print("enqueued:", x)

    def dequeue(self):
        x = None
        if self.q.head:
            x = self.q.head.data
            self.q.head = self.q.head.next
            print("Dequeued:", x)
        else:
            print("empty queue")

    def __str__(self):
        return self.q.__str__()
