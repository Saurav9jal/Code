### Sort a stack using recursion


def insertNum(list,num):
    if(len(list) == 0):
       list.append(num)
    else:
       if(num < list[-1]):
           num1 = list.pop()
           insertNum(list,num)
           list.append(num1)

def sortRecursive(list):
    if(len(list) == 0):
       return 
    else:
       num = list.pop()
       sortRecursive(list)
       insertNum(list,num)
    print(list)


list = [5,4,3,2,1]
sortRecursive(list)










