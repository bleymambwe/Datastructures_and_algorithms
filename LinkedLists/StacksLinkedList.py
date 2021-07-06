class StackLinkedList():
    def __init__(self,limit = None):
        self.limit = limit
        self.head = None
        self.tail = None
        self.len = 0
        self.next = None
    def underflow(self):
        assert not " Stack underflow!"
    def overflow(self):
        assert not " Stack overflow!"

    def addData(self,data):
        self.data = data
    def append(self,item):
        new_node = StackLinkedList()
        new_node.addData(item)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.len+= 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.len+= 1
    def deleteEnd(self):
        cur = self.head
        pre = cur
        lst= pre
        while cur:
            lst = pre
            pre = cur
            cur = cur.next

        #pre.next = None
        #self.tail = pre
        self.len-=1
        self.tail = lst
        lst.next = None


    def push(self,item):
        if self.len > self.limit:
            self.overflow()
        else:
            self.append(item)
    def peek(self):
        "since this is a FILO impl, tail is the last"
        return print(self.tail.data)
    def pop(self):
        if self.len > self.limit:
            self.overflow()

        else:
            self.deleteEnd()
    def checklen(self):
        if self.len <= 0:
            self.underflow()
        else:
            return print(self.len)
a = StackLinkedList(8)
a.push(0)
a.push(1)
a.push(2)
a.peek()
#a.pop()
#a.peek()
