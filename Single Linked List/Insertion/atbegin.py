class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class LinkedList:
    def __init__(self):
        self.head=None
    def print(self):
        n=self.head
        while n is not None:
            print(n.data,"->",end=" ")
            n=n.ref
        print("\n")
    def begin(self,data):
        newNode=Node(data)
        newNode.ref=self.head
        self.head=newNode
LL1=LinkedList()
LL1.head=Node("Mon")
e2=Node("tues")
e3=Node("wed")
LL1.head.ref=e2
e2.ref=e3
LL1.print()
LL1.begin("sun")
LL1.print()