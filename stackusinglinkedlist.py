class Node:
    def __init__(self,d):
        self.data= d
        self.next=None
class stack:
    def __init__(self):
        self.head=None
    def pushdata(self,d):
        newnode=Node(d)
        if self.head is None:
            self.head=newnode
        else:
            temp=self.head
            while temp.next is not None :
                temp=temp.next
            temp.next=newnode
    def popdata(self):
        if self.head==None:
            print("No data")
        elif self.head.next == None:
            self.head=None
        else:
            temp = self.head
            while temp.next is not None:
                prev=temp
                temp = temp.next
            prev.next=None
            temp=None

    def travs(self):
        printval = self.head
        while printval is not None:
            print(printval.data)
            printval = printval.next
stack1=stack()

stack1.pushdata(20)
stack1.pushdata(19)

stack1.popdata()


stack1.travs()
