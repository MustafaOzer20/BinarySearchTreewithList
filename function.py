def Node(data,tree):
    iter = tree
    if iter==[]:
        tree=[data,[None],[None]]
    else:
        control=0
        while iter!=[None]:
            attr=iter
            if iter[0]>data:
                iter=iter[1] #left
            elif iter[0]<data:
                iter=iter[2] #right
            else:
                control=1
                break
        if control!=1:
            n = [None]
            iter.remove(None)
            iter.append(data)
            iter.append(n) ; iter.append(n)
            if attr[1]==attr[2]:
                if attr[0]<data:
                    attr[1]=[None]
                else:
                    attr[2]=[None]
    return tree


def noneControl(iter,attr,num):
    if num==2:
        n=1
    else:
        n=2
    iter=iter[num]
    while iter[n]!=[None]:
        iter=iter[n]
    val = iter[0]
    iter.clear()
    iter.append(None)
    attr[0]=val
def deletion(data,tree):
    iter=tree
    if search(data,tree):
        while iter[0]!=data:
            if iter[0]>data:
                iter=iter[1] #left
            elif iter[0]<data:
                iter=iter[2] #right1
            attr=iter
        if iter[1]==[None] and iter[2]==[None]:
            if(iter[0]!=tree[0]):
                iter.clear()
                iter.append(None)
            else:
                tree=[]
                return tree            
            return f"{data} deleted."
        elif iter[1]==[None] and iter[2]!=[None]:
            noneControl(iter,attr,2)
        elif iter[1]!=[None] and iter[2]==[None]:
            noneControl(iter,attr,1)
        elif iter[1]!=[None] and iter[2]!=[None]:
            noneControl(iter,attr,2)
    else:
        return f"{data} is not found in tree."


def search(data,tree,mybool=False):
    iter=tree
    cur =[]
    if iter!=[]:
        while iter!=[None]:
            attr=iter
            if iter[0]>data:
                iter=iter[1] #left
                cur.append(1)
            elif iter[0]<data:
                iter=iter[2] #right
                cur.append(2)
            else:
                if mybool:
                    ls=[]
                    ls.append(attr)
                    ls.append(cur)
                    return ls
                return True
    return False


def max_min(tree,min=False):
    iter = tree
    if iter==[]:
        return "Tree is empty"
    else:
        while iter!=[None]:
            attr=iter
            if min:
                iter=iter[1]
            else:
                iter=iter[2]
        val = attr[0]
        return val


def predessorAndsuccessor(data,tree,num=1):# 1-predessor 2-successor
    if num==1:
        n=2
    elif num==2:
        n=1
    else:
        return f"Error! num must be 1 or 2"
    control=search(data,tree,True)
    if type(control)==list:
        iter=control[0]
        if iter[num]!=[None]:
            iter=iter[num]
            while iter[n]!=[None]:
                iter=iter[n]
            val = iter[0]
            return val
        else:
            cur=control[1]
            iter=tree
            ctrl=len(cur)-1
            if num==1:
                while ctrl>0:
                    for i in range(ctrl):
                        iter=iter[cur[i]]
                    if iter[0]<data:
                        return iter[0]
                    ctrl-=1
                if tree[0]<data:
                    return tree[0]
                return data
            else:
                while ctrl>0:
                    for i in range(ctrl):
                        iter=iter[cur[i]]
                    if iter[0]>data:
                        return iter[0]
                    ctrl-=1
                if tree[0]>data:
                    return tree[0]
                return data 

