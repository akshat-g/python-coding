class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.counter = 0

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

    def deleteNode(self, k):
        if self.head == None:
            return
        if k == 0:
            self.head = self.head.next
            return
        count = 1
        temp = self.head
        while count != k and temp != None:
            temp = temp.next
            count += 1

        if temp.next is not None:
            temp.next = temp.next.next

    def findFrequencyRecur(self, temp, k):
        if temp == None:
            return self.counter

        if temp.data == k:
            self.counter = self.counter + 1

        return findFrequencyRecur(temp.next, k)


    def findFrequency(self, k):
        print findFrequencyRecur(self.head, k)


    def nNodeFromEnd(self, n):
        temp = self.head
        i = 1
        while i < n and temp is not None:
            temp = temp.next
            i += 1

        if temp is None:
            print "Not Possible"
        else:
            curr = self.head
            while temp.next is not None:
                curr = curr.next
                temp = temp.next

            print curr.data



if __name__ == '__main__':
    # llist = LinkedList()
    # llist.head = Node(1)
    # second = Node(2)
    # third = Node(3)

    # llist.head.next = second
    # second.next = third

    # llist.printList()
    # llist.nNodeFromEnd(4)
    #llist.findFrequency(1)
    l = [1,2,3]
    l.insert(0, 0)
    for i in l:
        print i,
