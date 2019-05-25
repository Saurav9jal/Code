### Sorted insert for circular linked list

class Node(object):
      def __init__(self,data):
          self.data = data
          self.next = None
 


def insertInList(root,root1):
    while(1):
      if(root..next.data == root1.data):
           root1.next = root.next
           root.next = root1
      root = root.next
     


root = Node(3)
root.next = Node(7)
root.next.next = Node(9)
root.next.next = Node(11)
root.next = root













