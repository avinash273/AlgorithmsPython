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
        node_list = []
        while cur.next is not None:
            cur = cur.next
            node_list.append(cur.data)
        print(*node_list, sep="->")

    def kToLastElement(self, k):
        """
        Complexity:
        time: O(n)
        space: O(n)
        :param k:
        :return:
        """
        cur = self.head
        count = 0
        ktolast = []
        while cur.next is not None:
            cur = cur.next
            if count >= k:
                ktolast.append(cur.data)
            count += 1
        return ktolast


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

linked_list1.display()
ans = linked_list1.kToLastElement(3)

print(*ans, sep="->")