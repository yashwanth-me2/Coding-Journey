class Stack:
    def __init__(self,cap):
        self.cap=cap
        self.arr=[]

    def push(self,x):
        if len(self.arr)==self.cap:
            return
        self.arr.append(x)

    def pop(self):
        if self.arr:
            return self.arr.pop()
        return

    def peek(self):
        if self.arr:
            return self.arr[-1]
        return 
    
    def size(self):
        return len(self.arr)

    def isempty(self):
        return self.size()==0

st=Stack(3)
st.push(1)
st.push(2)
st.push(3)
st.push(4)
print(st.pop())
print(st.peek())
print(st.size())
st.pop()
st.pop()
print(st.isempty())
    
