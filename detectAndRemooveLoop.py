### Detect and Remove Loop in a Linked List

class Node(object):
      def __init__(self,data):
         self.data = data
         self.next = None




def detectAndRemoveLoop(root):
    if(root == None):
         return 
    dict = {}
    root1 = root
    while(1):
       if(root1.next in dict.keys()):
           break
       dict[root1] = 0
       root1 = root1.next
    root1.next = None
    while(root != None):
       print(root.data)
       root = root.next


root = Node(1)
root.next = Node(2)
root.next.next = Node(3)
root.next.next.next = Node(4)
root.next.next.next.next = Node(5)
root.next.next.next.next.next = root.next
detectAndRemoveLoop(root)


