####  Print nodes at k distance from root

class Node(object):
      def __init__(self,data):
          self.data = data
          self.left =  None
          self.right = None



def printKDistance(root,k,level):
    if(root == None):
        return 
    if(level == 0):
       print("data at {} distance from root {}".format(k,root.data))
    printKDistance(root.left,k,level-1)
    printKDistance(root.right,k,level-1)





root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(5)
root.right = Node(3)
root.right.left = Node(8)
printKDistance(root,2,2)















