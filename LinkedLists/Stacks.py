class StackList():
    def __init__(self,data = None):
        self.limit = data
        self.list = [None for i in range(self.limit)]
    def resize(self ,size):
        for i in range(size):
            self.list.append(None)
    def underflow(self):
        assert not "Underflow"

    def overflow(self):
        pass
    def push(self,item):
        self.list.append(item)
    def pop(self):
        if len(self.list) <= 0:
            self.underflow()
        else:
            self.list.pop()
    def peek(self):
        if len(self.list) <= 0:
            self.underflow()
        else:
          print(self.list[-1])
    def checklen(self):
        return print(len(self.list))
#
# s = StackList(4)
# s.checklen()
# s.resize(10)
# s.checklen()
# #s.pop()
# s.peek()
