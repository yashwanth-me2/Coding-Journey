class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

class Queue:
    def __init__(self,cap):
        self.cap=cap
        self.size=0
        self.front=None
        self.rear=None

    def enqueue(self,x):
        if self.size==self.cap:
            return
        temp=Node(x)
        if not self.size:
            self.front=self.rear=temp
            self.size+=1
        else:
            self.rear.next=temp
            self.rear=temp
            self.size+=1
    
    def dequeue(self):
        if not self.size:
            return
        x=self.front.val
        if self.size==1:
            self.front=self.rear=None
        else:
            self.front=self.front.next
        self.size-=1
        return x

