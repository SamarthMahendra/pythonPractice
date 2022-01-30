class Node:

    def __init__(self,data):
        self.data=data
        self.nextval=None
    def __repr__(self):
        return "<Node Data :%s" % self.data
class linkedlist:
    def __init__(self):
        self.head=None
    def trav(self):
        printval=self.head
        while printval is not None:
            print(printval.data)
            printval=printval.nextval
    def insertbeg(self,d):
        newnode=Node(d)
        newnode.nextval=self.head
        self.head=newnode
    def insertend(self,d):
        newnode = Node(d)
        if self.head is None:

            self.head=newnode
        else:
            laste=self.head
            while laste.nextval is not None:
                laste=laste.nextval
            laste.nextval=newnode
    def insertbetween(self,dk,d):
        if self.head is None:
            return print("list empty")
        else:
            temp=self.head
            while temp.data is not dk and temp.nextval is not None:
                temp=temp.nextval
            if temp.data is dk:
                newnode=Node(d)
                temp.nextval=newnode.nextval
                temp.nextval=newnode
            else:
                return print("Not found")
    def removenode(self,d):
        headval=self.head
        if (headval is not None):
            if (headval.data == d):
                self.head=headval.nextval
                headval=None
                return
        while (headval is not None):
            if headval.data==d:
                break
            prev=headval
            headval=headval.nextval
        if headval ==  None:
            return
        prev.nextval=headval.nextval
        headval = None
        print("Removed")



list1=linkedlist()
list1.head=Node("Mon")
e2=Node("Tue")
list1.head.nextval=e2
list1.insertbeg("Sun")
list1.insertbetween("Tue","sat")
list1.insertend("Wed")
list1.removenode("Tue")

list1.insertbetween("Wed","fri")
list1.trav()