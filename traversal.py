list_inorder=[]
list_preorder=[]
list_postorder=[]
def preorder(tree):
    if(tree[0]!=None):
        list_preorder.append(tree[0])
        preorder(tree[1])
        preorder(tree[2])
def postorder(tree):
    if(tree[0]!=None):
        postorder(tree[1])
        postorder(tree[2])
        list_postorder.append(tree[0])
def inorder(tree):
    if(tree[0]!=None):
        inorder(tree[1])
        list_inorder.append(tree[0])
        inorder(tree[2])






