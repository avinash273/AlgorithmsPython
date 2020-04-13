# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        def __init__(self):
            self.head = ListNode()

        while l1.next != None or l2.next != None:
            if l2.val != None and l1.val < l2.val:
                self.add_here(l1.val)
                l1 = l1.next
            elif l1.val != None and l1.val > l2.val:
                self.add_here(l2.val)
                l2 = l2.next

    def append(self, data):
        new_node = ListNode(data)
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

    def add_here(self, val):
        cur = self.head
        new_node = ListNode(val)
        while cur.next != None:
            cur = cur.next
            cur.next = new_node
        return cur

linked_list1 = Solution()
# print("Before:", linked_list1.length())
linked_list1.append(1)
linked_list1.append(2)
linked_list1.append(3)
linked_list1.append(4)
linked_list1.append(5)

linked_list1.display()