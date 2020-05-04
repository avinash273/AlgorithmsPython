class node:
    def __init__(self, data=0):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = node()

    def append(self, data=None):
        new_node = node(data)
        cur = self.head

        while cur.next is not None:
            cur = cur.next
        cur.next = new_node

    def display(self):
        cur = self.head
        array = []
        while cur.next is not None:
            cur = cur.next
            array.append(cur.data)
        print(*array, sep="->")

    def erase(self, val):
        cur = self.head

        while cur.next is not None:
            prev = cur
            cur = cur.next
            if cur.data == val:
                prev.next = cur.next

    def insert_at(self, loc, val):
        new_node = node(val)
        cur = self.head
        count = 0

        while cur.next is not None:
            prev = cur
            cur = cur.next
            count += 1

            if count == loc:
                prev.next = new_node
                new_node.next = cur
        # insert at end position not possible by this function need to fix
        if count < loc:
            cur.next = new_node


LinkedList = LinkedList()

LinkedList.append(1)
LinkedList.append(2)
LinkedList.append(3)
LinkedList.append(4)
LinkedList.append(5)

LinkedList.display()
LinkedList.insert_at(6, 8)
LinkedList.display()
LinkedList.insert_at(6, 9)
LinkedList.display()
