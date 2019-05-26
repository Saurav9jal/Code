### Program for n’th node from the end of a Linked List


class Node(object):
     def __init__(self,data):
         self.data = data
         self.next = None


def findLength(root):
     if(root == None):
       return 0
     count = 0
     while(root != None):
        count+=1
        root = root.next
     return count 

def nthNode(root,n):
    if(root == None):
        return 
    count = findLength(root)
    n = count - n
    while(1):
        n -= 1
        if( n == 0):
          print("the data is {}".format(root.data))
          break
        root = root.next

      


root = Node(1)
root.next = Node(4)
root.next.next = Node(5)
root.next.next.next = Node(2)
nthNode(root,2)



