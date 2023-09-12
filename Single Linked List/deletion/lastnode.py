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
            print("->",n.data,end=" ")
            n=n.ref
    def delete(self):
        if self.head is None:
            print("list empty")
        else:
            self.head=self.head.ref
    def last(self):
        if self.head is None:
            print("empty list")
        else:
            n=self.head
            while n.ref.ref is not None:
                n=n.ref
            n.ref=None
ll1=LinkedList()
ll1.head=Node("Mon")
e2=Node("tues")
e3=Node("wed")
ll1.head.ref=e2
e2.ref=e3
ll1.last()
ll1.print()
