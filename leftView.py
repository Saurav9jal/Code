### Print Left View of a Binary Tree

class Node(object):
      __maxvalue = 0
      def __init__(self,data):
          self.data = data
          self.left = None
          self.right = None



def printLeftView(root,level,list):
      if(root == None):
          return 
      if(list[0] < level):
         print("left view for level {} is {}".format(level,root.data))
         list[0] = level
      printLeftView(root.left,level+1,list)
      printLeftView(root.right,level+1,list)




root = Node(4)
root.left = Node(5)
root.right = Node(2)
root.right.left = Node(3)
root.right.left.left = Node(6)
root.right.right = Node(1)
root.right.left.right = Node(7)
list = [0]
printLeftView(root,1,list)


