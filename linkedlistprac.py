class node:
    def __init__(self,val):
        self.data=val
        self.next=None
class linkedlist:
    def __init__(self):
        head=None
    def printlist(self):
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.next
    def printrec(self,temp):

        while temp:
            print(temp.data)
            return self.printrec(temp.next)
        return None
    def reverselist(self):
        prev=None
        current=self.head

        while current:
            next = current.next
            current.next=prev
            prev=current
            current=next

        return prev
S=linkedlist()
a=node(1)
b=node(2)
c=node(3)
d=node(4)
S.head=a
S.head.next=b
b.next=c
c.next=d

a=S.reverselist()
S.printrec(a)



