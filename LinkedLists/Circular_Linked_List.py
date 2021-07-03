class CircularLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.next = None
        self.count =0
        self.len =0
    def addData(self,data):
        self.data = data
    def addlen(self):
        self.len+=1
    def sublen(self):
        self.len-=1
    def checklen(self):
        return print(self.len)
    def append(self,item):
        new_node = CircularLinkedList()
        new_node.addData(item)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.tail.next = self.head

            self.addlen()
        else:
            self.tail.next = new_node
            self.tail  = new_node
            self.tail.next = self.head
            self.addlen()
    def counting(self):
        self.count+=1

    def traverse(self):
        cur = self.head
        ref = cur is self.tail

        while cur and self.count != self.len:
            print(cur.data)
            cur = cur.next

            self.counting()
a = CircularLinkedList()
a.append(0)
a.append(1)
a.append(2)
a.append(3)
#a.checklen()
a.traverse()
