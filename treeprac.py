class node:
    def __init__(self,key):
        self.data=key
        self.left=None
        self.right=None
def inorder(root):
    if root!=None:
        inorder(root.left)
        print(root.data)
        inorder(root.right)
def insert(root,key):
    if root==None:
        root=node(key)
    q=[]
    q.append(root)
    temp=root
    while len(q):
        temp=q[0]
        q.pop(0)
        if temp.left == None:
            temp.left=node(key)
            return
        else:
            q.append(temp.left)
        if temp.right==None:
            temp.right=node(key)
            return
        else:
            q.append(temp.right)
def delelast(root,temp):
    q=[]
    q.append(root)
    while len(q):
        root=q[0]
        q.pop(0)
        if root==temp:
            root=None
            return
        if root.left!=None:
            if root.left==temp:
                root.left=None
                return
            else:
                q.append(root.left)
        if root.right!=None:
            if root.right==temp:
                root.right=None
                return
            else:
                q.append(root.right)

def dele(root,key):
    if root==None:
        return
    if root.left == None and root.right == None:
        if root.data==key:
            return None
        else:
            return root
    q=[]
    temp=root
    keynode=None
    q.append(temp)
    while(len(q)):
        temp=q[0]
        q.pop(0)
        if temp.data==key:
            keynode=temp
        if temp.left!=None:
            q.append(temp.left)
        if temp.right!=None:
            q.append(temp.right)
    if keynode!=None:
        x=temp.data
        delelast(root,temp)
        keynode.data=x
    return root
root=node(10)
root.right=node(20)
root.left=node(5)
root.right.left=node(15)
root.right.right=node(25)
inorder(root)
insert(root,11)
print("after insertion")
inorder(root)
root=dele(root,5)
print(("after del"))
inorder(root)