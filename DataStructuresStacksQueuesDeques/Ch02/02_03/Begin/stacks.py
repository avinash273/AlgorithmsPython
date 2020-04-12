class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        """
        Works in constant time O(1) complexity
        """
        self.items.append(item)

    def pop(self):
        """
        Removes the last item, which is O(1) time operation
        """
        if self.items:
            return self.items.pop()
        else:
            return None

    def peek(self):
        """
        This will return the item at top
        O(1) time operation
        :return:
        """
        if self.items:
            return self.items[-1]
        else:
            return ""

    def size(self):
        """
        runs in O(1) is constant time operation
        :return:
        """
        if self.items:
            return len(self.items)
        else:
            return ""

    def is_empty(self):
        if self.items:
            return False
        else:
            return True


Stack = Stack()
print("Is empty", Stack.is_empty())
Stack.push(1)
Stack.push(2)
Stack.push(3)
Stack.push(4)
Stack.push(5)
Stack.push(6)
print("Is empty", Stack.is_empty())
print("Items: ", Stack.items)

print("Peek ", Stack.peek())
print("Size ", Stack.size())
print("pop ", Stack.pop())
print("After pop ", Stack.items)
print("Size ", Stack.size())

print("Size ", Stack.size())
