class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while temp != None:
            print (temp.data)
            temp = temp.next

    def reverseList(self):
        if self.head == None or self.head.next == None:
            return
        else:
            temp = self.head
            temp1 = temp.next
            temp.next = None

            while temp1 is not None:
                temp2 = temp1.next
                temp1.next= temp
                temp = temp1
                temp1 = temp2

            self.head = temp






if __name__ == '__main__':
    llist = LinkedList()
    llist.head = Node(1)
    # second = Node(2)
    # third = Node(3)

    # llist.head.next = second
    # second.next = third

    llist.printList()
    llist.reverseList()
    llist.printList()
