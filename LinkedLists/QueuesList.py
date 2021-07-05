class QueueList():
    'First in first out'
    def __init__(self):
        self.list = []
    def enQueue(self,item):
        self.list.append(item)
    def deQueue(self):
        assert not len(self.list) == 0, "Queue empty"
        self.list.pop(0)
    def checklen(self):
        return print(len(self.list))
a = QueueList()
a.deQueue()
