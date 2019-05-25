###Write Code to Determine if Two Trees are Identical

class Node(object):
   def __init__(self,data):
       self.data = data
       self.left = None
       self.right = None



def checkIdentical(root,root1):
    if(root == None and root1 == None):
         return True
    if((root == None and root1 != None ) or (root != None and root1 == None)):
         return False
    if((root.data == root1.data) and (checkIdentical(root.left,root1.left)) and (checkIdentical(root.right,root1.right))):
         return True
    return False


root = Node(5)
root.left = Node(1)
root.right = Node(3)

root1 = Node(5)
root1.left =  Node(1)
root1.right = Node(4)

print(checkIdentical(root,root1))






