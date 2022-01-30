class node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.data=key
class tree:
    def __init__(self,):
        self.root=None
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)
def levelorderinsertion(temp,key):
    if not temp:
        temp=node(key)
        return
    q=[]
    q.append(temp)
    while(len(q)):
        temp=q[0]
        q.pop(0)
        if not temp.left :
            temp.left=node(key)
            return
        else:
            q.append(temp.left)
        if not temp.right:
            temp.right=node(key)
            return
        else:
            q.append(temp.right)

def mirror(temp):
    if temp == None:
        return
    else:
        mirror(temp.left)
        mirror(temp.right)
        temp.left,temp.right=temp.right,temp.left

t=tree()
t.root=node(10)
t.root.left=node(5)
t.root.right=node(15)
inorder(t.root)
levelorderinsertion(t.root,2)
print("after inserion")
inorder(t.root)

mirror(t.root)
print("after mirror")
inorder(t.root)






