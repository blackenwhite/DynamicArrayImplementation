
#implementation of a tree in Python3 as a list of lists :)
myTree=['a',#root
        ['b', #left subtree
         ['d',[],[]],
         ['e',[],[]]],
         ['c', #right subtree
          ['f',[],[]],
          []]
         ]

#making this kind of  binary  tree         
def BinaryTree(r):
    return [r,[],[]]
#inserting the left child
def insert_left(root,newBranch):
    t=root.pop(1)
    if len(t)>1:
        root.insert(1,[newBranch,t,[]])
    else:
        root.insert(1,[newBranch,[],[]])
    return root

#insering the right child
def insert_Right(root,newBranch):
    t=root.pop(2)
    if len(t)>1:
        root.insert(2,[newBranch,[],t])
    else:
        root.insert(2,[newBranch,[],[]])
    return root

#access functions
def GetRootvalue(root):
    return root[0]

def setRootVal(root,newVal):
    root[0]=newVal
    return

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]


#implementation of a tree
r=BinaryTree(3)
insert_left(r,4)
insert_Right(r,5)