class Node: 
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.val = key


def insertTree(root, n):
    a = [5, 2, 8, 3, 4, 6]
    i=1
    local=1
    #root = Node(a[0])
    while i< n:
        local = 1
        root = Node(a[0])
        print('root value'+str(root.val))
        while(local==1):
            if (a[i]>root.val):
                print(a[i])
                print(root.right)
                if root.right is None:
                    root.right = a[i]
                    local = 0
                    print('exit')
                else:
                    print('second lop')
                    print(root.right)
                    root = Node(root.right)
                    print(root.val)
                    local =1
            else:
                if (a[i]<root.val):
                    if root.left is None:
                        root.left = a[i]
                        local =0
                    else:
                        root = root.left
                        local =1
        i+=1
        #return root
        
def inOrder(root): 
    if root != None: 
        inOrder(root.left)  
        print(root.val,end=" ")  
        inOrder(root.right)

if __name__ == '__main__': 
    a = [1, 2, 3, 4, 5, 6] 
    n = len(a)
    #i =1
    local =1
    root = insertTree(a[0],n)
    inOrder(root) 
