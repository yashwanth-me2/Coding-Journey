class Queue:
    def __init__(self,cap):
        self.cap=cap
        self.arr=[None]*cap
        self.front=-1
        self.rear=-1
        self.size=0

    def enqueue(self,x):
        if self.size==self.cap:
            return
        if self.size==0:
            self.front=self.rear=0
        else:
            self.rear=(self.rear+1)%self.cap
        self.arr[self.rear]=x
        self.size+=1
    
    def dequeue(self):
        if self.size==0:
            return
        x=self.arr[self.front]
        self.arr[self.front]=None
        if self.size==1:
            self.front=self.rear=-1
        else:
            self.front=(self.front+1)%self.cap
        self.size-=1
        return x


