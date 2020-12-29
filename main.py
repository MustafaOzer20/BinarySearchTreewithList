from function import *
from traversal import *

tree=[]
while True:
    print("""
*************************************************
        1.Print the tree
        2.Add a node
        3.Deletion
        4.Search
        5.Min Value
        6.Max Value
        7.Predessor
        8.Successor
        9.Postorder
        10.Inorder
        11.Preorder
        12.Exit
*************************************************
    """)
    try:
        choice=int(input("Choose action : "))
        if choice==1:
            print(tree)
        elif choice==2:
            data = int(input("Enter the value to add : "))
            tree = Node(data,tree)
        elif choice==3:
            data = int(input("Enter the value to delete : "))
            control = deletion(data,tree)
            if type(control)==list:
                print(f"{tree[0]} deleted.")
                tree=control
            else:
                print(control)
        elif choice==4:
            data = int(input("Enter the value to search : "))
            print(search(data,tree))
        elif choice==5:
            print("Min Value : ",max_min(tree,True))
        elif choice==6:
            print("Max Value : ",max_min(tree))
        elif choice==7:
            data = int(input("Enter the value of predessor : "))
            print(predessorAndsuccessor(data,tree))
        elif choice==8:
            data = int(input("Enter the value of successor : "))
            print(predessorAndsuccessor(data,tree,2))
        elif choice==9:
            preorder(tree)
            print("Preorder : ",list_preorder)
            list_preorder.clear()
        elif choice==10:
            inorder(tree)
            print("Inorder : ",list_inorder)
            list_inorder.clear()
        elif choice==11:
            postorder(tree)
            print("Postorder : ",list_postorder)
            list_postorder.clear()
        elif choice==12:
            print("Exit...")
            break
        else:
            print("Error.!")
    except:
        print("Error.!")




