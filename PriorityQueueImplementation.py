class PriorityQueue:

    def __init__(self, maxsize):
        self.size = 0
        self.heap = [0]*maxsize

    def push(self, value):
        if self.size == len(self.heap):
            print "cannot push; heap is full"
            return

        pos = self.size
        self.heap[pos] = value

        while pos > 0:
            parent = (pos - 1)/2
            if self.heap[parent] >= self.heap[pos]:
                print "parent already bigger than child"
                break
            else:
                self._swap(pos, parent)
                pos = parent

        self.size += 1

    def pop(self):
        if self.size == 0:
            print "cannot pop; since the heap is empty"
            return

        poppedItem = self.heap[0]
        self.heap[0] = self.heap[self.size-1]
        self.size = self.size - 1

        pos = 0
        while pos < self.size/2:
            leftChild = 2 * pos + 1
            rightChild = leftChild + 1

            if rightChild < self.size and self.heap[rightChild] > self.heap[leftChild]:
                if self.heap[pos] < self.heap[rightChild]:
                    self._swap(pos, rightChild)
                    pos = rightChild

            else:
                if self.heap[pos] < self.heap[leftChild]:
                    self._swap(pos, leftChild)
                    pos = leftChild

        return poppedItem

    def _swap(self, i, j):
        temp = self.heap[i]
        self.heap[i] = self.heap[j]
        self.heap[j] = temp

    def printPQ(self):
        print self.heap


pq = PriorityQueue(7)
pq.printPQ()
pq.push(4)
pq.printPQ()
pq.push(3)
pq.printPQ
pq.push(5)
pq.printPQ()
pq.push(6)
pq.printPQ()
pq.pop()
pq.printPQ()
print pq.size
