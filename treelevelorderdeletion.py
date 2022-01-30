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
def deleteDeepest(root,d_node):
    q = []
    q.append(root)
    while (len(q)):
        temp = q.pop(0)
        if temp is d_node:
            temp = None
            return
        if temp.right:
            if temp.right is d_node:
                temp.right = None
                return
            else:
                q.append(temp.right)
        if temp.left:
            if temp.left is d_node:
                temp.left = None
                return
            else:
                q.append(temp.left)
def deletion(root, key):
    if root == None :
        return None
    if root.left == None and root.right == None:
        if root.key == key :
            return None
        else :
            return root
    key_node = None
    q = []
    q.append(root)
    temp = None
    while(len(q)):
        temp = q.pop(0)
        if temp.data == key:
            key_node = temp
        if temp.left:
            q.append(temp.left)
        if temp.right:
            q.append(temp.right)
    if key_node :
        x = temp.data
        deleteDeepest(root,temp)
        key_node.data = x
    return root





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

print("after inserion")
inorder(t.root)

mirror(t.root)
print("after mirror")
inorder(t.root)
t.root=deletion(t.root,10)
print("after d")
inorder(t.root)





