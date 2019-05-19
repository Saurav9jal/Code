#### Write Code to Determine if Two Trees are Identical

class Node(object):
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None






def checkIdentical(root1,root2):
    if(root1 == None and root2 == None):
        return True
    if(root1 != None and root2 == None):
        return False
    if(root1 == None and root2 != None):
        return False  
    if((root1.data == root2.data) and checkIdentical(root1.left,root2.left) and checkIdentical(root1.right,root2.right)):
        return True
    return False



root1 = Node(1)
root2 = Node(1)
root1.left = Node(2)
root1.right = Node(3)
root2.left= Node(2)
root2.right = Node(3)
print(checkIdentical(root1,root2))














