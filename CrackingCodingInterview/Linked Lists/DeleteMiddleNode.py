import math

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = Node()

    def append(self, data):
        cur = self.head
        new_node = Node(data)

        while cur.next is not None:
            cur = cur.next
        cur.next = new_node

    def display(self):
        cur = self.head
        display_node = []
        while cur.next is not None:
            cur = cur.next
            display_node.append(cur.data)
        print(*display_node, sep="->")

    def delete_middle(self):
        cur = self.head
        length = 0
        while cur.next is not None:
            length += 1
            cur = cur.next

        middle = math.floor(length/2)
        print(middle)

        count = 0
        cur = self.head
        while cur.next is not None:
            count += 1
            last = cur
            cur = cur.next
            if count == middle:
                last.next = cur.next
                cur = last
        print(cur)


linked_list1 = LinkedList()
linked_list1.append(0)
linked_list1.append(1)
linked_list1.append(2)
linked_list1.append(3)
linked_list1.append(4)
linked_list1.append(5)
linked_list1.append(6)
linked_list1.append(7)
linked_list1.append(8)
linked_list1.append(2)
linked_list1.append(3)
linked_list1.append(4)
linked_list1.append(5)
linked_list1.append(6)
linked_list1.append(7)
linked_list1.append(8)

print(linked_list1)

linked_list1.display()

linked_list1.delete_middle()

linked_list1.display()
