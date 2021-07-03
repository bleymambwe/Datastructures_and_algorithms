
class Linkedlist:
    def __init__(self):
        self.head= None
        self.next = None
        self.len  = 0
        self.counter = 0

    def addData(self,data):
        self.data= data

    def append(self,data):
        new_node = Linkedlist()
        new_node.addData(data)

        if self.head == None:
            self.head = new_node
            self.tail = self.head
            self.len+= 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.len+= 1

    def prepend(self,data):
        new_node = Linkedlist()
        new_node.addData(data)

        if self.head == None:
            self.head = new_node
            self.tail = new_node
            self.len+= 1
        else:
            new_node.next = self.head
            self.head = new_node
            self.len+= 1
    def checkempty(self):
        if self.head == None:
            return True
        else:
            return False

    def traverse(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next
    def insert(self,item,pos):
        new_node = Linkedlist()
        new_node.addData(item)
        cur = self.head
        pre = cur
        while cur and self.counter != pos:
            self.counter+= 1
            cur = pre
            cur = cur.next
        if cur == self.head and self.head is None:
            assert not "list empty"
        if pos == 0:
            self.append(item)
        elif pos == self.len:
            self.tail.next = new_node
            self.tail = new_node
        elif  pos > 0 and pos <= self.len+1:
            pre.next = new_node
            new_node.next = cur
        else:
            assert not "pos out of bound"


    def delete(self,item):
        pre = None
        cur= self.head

        while cur and cur.data != item:
            pre = cur
            cur = cur.next

        if cur is not None:
            if cur.data == item:
                self.head.next = self.head
            else :
                pre.next = cur.next



a = Linkedlist()
a.append(0)
a.append(1)
a.append(2)
a.traverse()
a.insert(pos = 1,item = 5)
a.traverse()
#a.delete(0)
#a.traverse()
#a.prepend(0)
#a.prepend(1)
#a.traverse()
