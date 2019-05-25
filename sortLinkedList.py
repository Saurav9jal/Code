### Sort a linked list of 0s, 1s and 2s

class Node(object):
     def __init__(self,data):
         self.data = data
         self.next = None



def printList(root):
    while(root!= None):
       print("element is :{}".format(root.data))
       root = root.next

def sortList(root):
    count0 = 0
    count1 = 0
    count2 = 0
    rootI = root
    while(rootI!= None):
      if(rootI.data == 0):
         count0+=1
      if(rootI.data == 1):
         count1+=1
      if(rootI.data == 2):
         count2+=1
      rootI= rootI.next
    while(count1 !=0 or count0 != 0 or count2 != 0 ):
      if(count0 !=0):
         root.data = 0
         count0-=1
      elif (count1!= 0):
         root.data = 1
         count1-=1
      else:
         root.data = 2
         count2 -=1
      root = root.next
           

root = Node(0)
root.next = Node(1)
root.next.next = Node(0)
root.next.next.next = Node(2)
root.next.next.next.next = Node(1)
sortList(root)
printList(root)










