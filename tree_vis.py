import graphviz
import tkinter as tk
import os
from tkinter import messagebox
import PIL.Image
from PIL import ImageTk
st=[]
class Node :
    def __init__(self,data):
        
        self.data = data
        self.left = None
        self.right = None
class Tree:
    
    def __init__(self):
        
        self.root = None
        self.nodes=""

    def addnode(self,data):
        cur_node = Node(data)#取得node
        if cur_node.data not in st:#防止輸入同樣的數字
            st.append(cur_node.data)
            print(*st,sep=" ")
            
            if self.root is None:
                self.root = cur_node# root
            else:
                
                parent = None
                tmp = self.root
                while tmp is not None:
                    parent = tmp# 父節點
                    if int(cur_node.data)<int(tmp.data):
                        tmp = tmp.left#左子
                    elif int(cur_node.data)>int(tmp.data):
                        tmp  = tmp.right#右子
                if int(cur_node.data)<int(parent.data):
                    parent.left = cur_node
                else:
                    parent.right = cur_node
                
            
        else:
            
            messagebox.showinfo("input error",cur_node.data)
    """
    刪除葉子節點
    刪除只有一棵子樹的節點
    刪除有兩棵子樹的節點
    """
    def deletenode(self, data):
        self.root = self._deletenode(self.root, data)

    def _deletenode(self, node, key):
        if node is None:
            return node

        if int(key) < int(node.data):
            node.left = self._deletenode(node.left, key)
        elif int(key) > int(node.data):
            node.right = self._deletenode(node.right, key)
        else:
            # Node with only one child or no child
            if node.left is None:
                temp = node.right
                node = None
                return temp
            elif node.right is None:
                temp = node.left
                node = None
                return temp

            # Node with two children: Get the inorder successor (smallest in the right subtree)
            temp = self._minvalue(node.right)
            node.data = temp.data
            node.right = self._deletenode(node.right, temp.data)
        return node

    def _minvalue(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder(self,root):
        if root!=None:
            self.postorder(root.left)
            self.nodes  +=  root.data + " "
            self.postorder(root.right)
           
    def preorder(self,root):
        if root!=None:
            self.nodes  +=  root.data + " "
            self.postorder(root.left)
            self.postorder(root.right)

    def postorder(self,root):
        if root!=None:
            self.postorder(root.left)
            self.postorder(root.right)
            self.nodes  +=  root.data + " "
    
    def visualizetree(self,root):
        dot = graphviz.Digraph()
        dot.node(str(root.data))
        self.addedge(root,dot)
        dot.render("tree",format="png")

    def addedge(self,node,dot):
        if node.left:
            dot.node(str(node.left.data))
            dot.edge(str(node.data),str(node.left.data))
            self.addedge(node.left,dot)
        if node.right:
            dot.node(str(node.right.data))
            dot.edge(str(node.data),str(node.right.data))
            self.addedge(node.right,dot)
def add():
    tree.addnode(txtvalue.get())
    tree.visualizetree(tree.root)
    img =ImageTk.PhotoImage(PIL.Image.open("tree.png"))
    lblimage.configure(image=img)
    lblimage.image = img 
def delete():

    tree.deletenode(txtvalue.get())
    tree.visualizetree(tree.root)
    img = ImageTk.PhotoImage(PIL.Image.open("tree.png"))
    lblimage.configure(image=img)
    lblimage.image = img
def inorder():
    tree.inorder(tree.root)
    messagebox.showinfo("inorder",tree.nodes)
    tree.nodes = ""

def preorder():
    tree.preorder(tree.root)
    messagebox.showinfo("preorder",tree.nodes)
    tree.nodes = ""

def postorder():
    tree.postorder(tree.root)
    messagebox.showinfo("Postorder",tree.nodes)
    tree.nodes = ""

def showimage(event):
    os.system("tree.png") if os.path.exists("tree.png") else None

def clear():
    global tree
    tree = Tree()
    st.clear()
    lblimage.configure(image='')
if __name__ == "__main__":

    tree = Tree()
    root = tk.Tk()
    root.title("my bst tree")
    root.geometry("1300x1300")

    lblvalue = tk.Label(root,text = "Enter tree node data: ")# 輸入框的字
    lblvalue.place(x=0,y=50,width=150)

    txtvalue = tk.Entry(root)#輸入框填值
    txtvalue.place(x=150,y=50,width=100)
    
    btnadd = tk.Button(root,text="add",command=add)
    btnadd.place(x=50,y=100,width=100)

    btninorder = tk.Button(root,text="inorder",command=inorder)
    btninorder.place(x=150,y=100,width=100)

    btnpreorder = tk.Button(root,text="preorder",command=preorder)
    btnpreorder.place(x=50,y=150,width=100)
    
    btnpostorder = tk.Button(root,text="postorder",command=postorder)
    btnpostorder.place(x=150,y=150,width=100)
    
    btnclear = tk.Button(root,text="clear",command=clear)
    btnclear.place(x=150,y=200,width=100)

    btndelete = tk.Button(root,text= "delete node",command=delete)
    btndelete.place(x=50,y=200,width=100)
    #圖片
    lblimage = tk.Label(root)
    lblimage.bind("<Button-1>",showimage)
    lblimage.place(x=300,y=50,width=1000,height=1000)
    root.mainloop()

    if os.path.exists("tree.png"):
        os.remove("tree.png")
        os.remove("tree")

                

