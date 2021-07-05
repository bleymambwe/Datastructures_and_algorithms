class QueueCircular:
    def __init__(self,limit = None):
        self.limit = limit
        self.front = None
        self.rear = None
        self.next = None
        self.len = 0
    def addData(self,data):
        self.data = data
    def underflow(self):
        assert not "Queue underflow"
    def overflow(self):
        assert not "Queue overflow"
    def append(self,item):
        new_node = QueueCircular()
        new_node.addData(item)
        if self.front is None:
            self.front = new_node
            self.rear = new_node
            self.len+=1
        else:
            self.rear.next = new_node
            self.rear = new_node
            self.rear.next  = self.front
            self.len+=1

    def enQueue(self,item):
        if self.len == self.limit:
            self.overflow()
        else:
            self.append(item)
    def deQueue(self):
        if self.len ==0:
            self.underflow()
        else:
            self.front= self.front.next
            self.rear.next = self.front

    def peek(self):
        return print(self.front.data)


a = QueueCircular(5)
a.enQueue(0)
a.enQueue(1)
a.enQueue(2)
a.deQueue()

a.peek()
