class Queue:

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """
        Inserts an item at the zeroth index of the Queue.
        The runtime will be O(n), because inserting into the zeroth index forces all the elements to move by one.
        :param item:
        :return:
        """
        self.items.insert(0, item)

    def dequeue(self):
        """
        :return: front most item from equeue
        works in constant time O(1)
        """
        self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def is_empty(self):
        if self.items:
            return False
        else:
            return True


myQueue = Queue()
myQueue.enqueue('apple')
myQueue.enqueue('banana')
myQueue.enqueue('orange')
print(myQueue.items)
myQueue.dequeue()
print(myQueue.items)

print(myQueue.is_empty())