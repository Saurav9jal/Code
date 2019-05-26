### Print all nodes in a binary tree having K leaves


class  Node(object):
      def __init__(self,data):
         self.data = data
         self.left = None
         self.right = None




def printNodeHavingK(root,k):
    if(root == None):
       return 0
    if(root.left == None and root.right == None):
       return 1
    leftTree = printNodeHavingK(root.left,k)
    rightTree = printNodeHavingK(root.right,k)
    if((leftTree + rightTree) == k):
        print("data is {}".format(root.data))
    return (leftTree + rightTree)  
    

root = Node(1)
root.left = Node(3)
root.left.left = Node(5)
root.left.right = Node(9)
root.right = Node(6)
root.right.left = Node(8)
root.right.right = Node(7)
printNodeHavingK(root,2)





