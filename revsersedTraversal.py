### Reverse Level Order Traversal

class Node(object):
      def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


def levelOrderT(root,dict,level):
    if(root == None):
       return 
    if(level in dict.keys()):
        dict[level].append(root.data)
    else:
        dict[level] = [root.data]
    levelOrderT(root.left,dict,level+1)
    levelOrderT(root.right,dict,level+1)  


dict ={}
root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(5)
root.right = Node(3)
levelOrderT(root,dict,0)
print(dict)        












