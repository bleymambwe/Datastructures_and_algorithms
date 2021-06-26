
class Linkedlist:
    def __init__(self):
        self.head= None
        self.next = None
        self.len  = 0

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


    def traverse(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next
    def delete(self,pos):
        i
        "delete at start"



a = Linkedlist()
a.checkempty()
#a.append(0)
#a.append(2)
#a.traverse()

#a.prepend(0)
#a.prepend(1)
#a.traverse()
