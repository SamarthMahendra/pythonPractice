class node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.val=data
def insert(temp,key):
    '''level order insertion'''
    if not temp:
        temp=node(key)
        return
    q=[]
    q.append(temp)
    while (len(q)):
        temp=q[0]
        q.pop(0)
        if( not temp.left):
            temp.left=node(key)
            break
        else:
            q.append(temp.left)
        if not temp.right:
            temp.right=node(key)
            break
        else:
            q.append(temp.right)

def inorder(root):
    if root != None:
        inorder(root.left)
        print(root.val)
        inorder(root.right)


root = node(10)
root.left = node(11)
root.left.left = node(7)
root.right = node(9)
root.right.left = node(15)
root.right.right = node(8)
inorder(root)
print("Before insertion")
insert(root,12)
inorder(root)