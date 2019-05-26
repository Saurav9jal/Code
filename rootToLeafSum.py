#### Root to leaf path sum equal to a given number


class Node(object):
      def __init__(self,data):
         self.data = data
         self.left = None
         self.right = None



def findSum(root,sum,pre):
    if(root == None):
        return 
    sum += root.data
    if(sum == pre):
       print("True")
    findSum(root.left,sum,pre)
    findSum(root.right,sum,pre)


root = Node(10)
root.left = Node(8)
root.right = Node(2)
root.right.left = Node(2)
root.left.left = Node(3)
root.left.right = Node(5)

findSum(root,0,15)








