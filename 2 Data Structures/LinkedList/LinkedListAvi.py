# Linked List
class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

    def get_data(self):
        return self.val

    def set_data(self,val):
        self.val = val

    def get_next(self):
        return self.next

    def set_next(self,next):
        self.next = next

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        self.count = 0

    def get_count(self):
        return self.count

    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node
        self.count += 1

    def dump_list(self):
        tempnode = self.head
        while(tempnode!= None):
            print("Node: ", tempnode.get_data())
            tempnode = tempnode.get_next()

    def find(self,val):
        found = self.head
        while(found != None):
            if(found.get_data() == val):
                print("Found", val)
                return found
            else:
                found = found.get_next()
        return None

    def deleteAt(self,idx):
        if idx > self.count:
            return
        if self.head == None:
            return
        else:
            tempIdx = 0
            node = self.head
            while tempIdx < idx-1:
                node = node.get_next()
                tempIdx += 1
            node.set_next(node.get_next().get_next())
            self.count -= 1

itemlist = LinkedList()
itemlist.insert(50)
itemlist.insert(40)
itemlist.insert(30)
itemlist.insert(20)
itemlist.insert(10)

itemlist.dump_list()

itemlist.find(200)

itemlist.deleteAt(3)

print("\n")

itemlist.dump_list()


