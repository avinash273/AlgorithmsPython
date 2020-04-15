class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = Node()

    def append(self, data):
        new_node = Node(data)
        cur = self.head

        while cur.next is not None:
            cur = cur.next
        cur.next = new_node

    def display(self):
        cur = self.head
        listData = []
        while cur.next is not None:
            cur = cur.next
            listData.append(cur.data)
        print(*listData, sep="->")


linked_list1 = LinkedList()
linked_list1.append(1)
linked_list1.append(2)
linked_list1.append(3)
linked_list1.append(4)
linked_list1.append(5)

linked_list1.display()
