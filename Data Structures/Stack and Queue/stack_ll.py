class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

class Stack:
    def __init__(self,cap):
        self.head=None
        self.cap=cap
        self.size=0

    def push(self,x):
        if self.size==self.cap:
            return
        temp=Node(x)
        temp.next=self.head
        self.head=temp
        self.size+=1
    
    def pop(self):
        if self.size:
            x=self.head.val
            self.head=self.head.next
            self.size-=1
            return x
        else:
            return
    
    def peek(self):
        if self.size:
            return self.head.val
        else:
            return
    
    def isempty(self):
        return self.size==0
    
    def isfull(self):
        return self.size==self.cap
    