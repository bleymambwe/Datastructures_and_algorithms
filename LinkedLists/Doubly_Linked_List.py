class Doublylinkedlist():
    def __init__(self):
        self.head = None
        self.next = None
        self.prev = None
        self.tail = None
        self.len = 0
        self.count = 0

    def counting(self):
        self.count+=1

    def addData(self,data):
        self.data =data

    def append(self,item):
        new_node = Doublylinkedlist()
        new_node.addData(item)

        if self.head is None:
            self.head = new_node
            self.tail =  new_node
            self.len+= 1
        else:
            self.tail.next =  new_node
            new_node.prev = self.tail
            self.tail = new_node
            self.len+= 1

    def prepend(self,item):
        new_node = Doublylinkedlist()
        new_node.addData(item)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.len+=1
        else:
            self.head.pre = new_node
            new_node.next = self.head
            self.head = new_node
            self.len+=1

    def traverse_backwards(self):
        cur = self.tail
        while cur:
            print(cur.data)
            cur = cur.prev
    def traverse_forward(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next
    def search(self,item):
        cur = self.head
        while cur !=None and cur.data != item:
            self.counting()
            cur = cur.next
        print(cur.data ,"is on pos", self.count )
    def insert(self,item,pos):
        new_node = Doublylinkedlist()
        new_node.addData(item)
        cur = self.head
        pre = cur

        if pos == 0:
            self.prepend(item)
        elif pos  == self.len:
            self.append(item)
        elif pos < 0 or pos < (self.len+1):
            assert not "Position out of bound"
        elif cur is None:
            assert not "List empty"

        while cur and self.count != pos:
            pre =cur
            self.counting()
            cur = cur.next
        pre.next = new_node
        new_node.next = cur
    def delete(self,item):
        cur =self.head
        pre =cur
        if cur == self.head and self.head is None:
            assert "List empty! "
        while cur and item != cur.data:
            cur = pre
            cur = cur.next
        cur.prev = cur.prev.prev
        cur.prev.prev.next = cur
        #cur.pre =  None


a = Doublylinkedlist()
a.append(0)
a.append(1)
a.append(2)
a.append(3)
a.append(4)
a.prepend(-1)

#a.traverse_forward()
a.traverse_backwards()
a.delete(3)
#a.insert(item = 6,pos = 0)
#a.traverse_forward()
