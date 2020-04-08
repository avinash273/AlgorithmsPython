class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class linked_list:
    def __init__(self):
        self.head = node()

    def append(self, data):
        new_node = node(data)
        cur = self.head

        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    def display(self):
        cur = self.head
        listData = []
        while cur.next is not None:
            cur = cur.next
            listData.append(cur.data)
        print(*listData, sep="->")

    def length(self):
        cur = self.head
        count = 0
        while cur.next is not None:
            cur = cur.next
            count += 1
        return count

    def get(self, index):
        cur = self.head
        count = 0
        while cur.next is not None:
            cur = cur.next
            if(count == index):
                return cur.data
            count += 1

    def erase(self, data):
        cur = self.head
        count = 0
        found = 0
        while cur.next is not None:
            last = cur
            cur = cur.next
            if cur.data == data:
                found += 1
                if count == 0:
                    self.head = cur
                    print("Deleted")
                    break
                else:
                    last.next = cur.next
                    print("Deleted")
                    break
            count += 1
        if found == 0:
            print("Element not found")

    def insert_node_at(self, index, data):
        cur = self.head
        ins_node = node(data)
        count = 0
        if index == count:
            ins_node.next = cur.next
            cur.next = ins_node
        else:
            while cur.next is not None:
                cur = cur.next
                cur2 = cur
                count += 1
                if(count == index):
                    ins_node.next = cur.next
                    cur.next = ins_node






linked_list1 = linked_list()
# print("Before:", linked_list1.length())
linked_list1.append(1)
linked_list1.append(2)
linked_list1.append(3)
linked_list1.append(4)
linked_list1.append(5)

# linked_list1.display()
# print("After:", linked_list1.length())
# print("At index:", linked_list1.get(2))

# linked_list1.erase(9)
# linked_list1.erase(4)
# linked_list1.display()
# print("After erase:", linked_list1.length())

# print("here")
linked_list1.insert_node_at(0,9)
linked_list1.insert_node_at(2,10)
linked_list1.insert_node_at(2,10)
linked_list1.display()
print("after display")
print("After erase:", linked_list1.length())