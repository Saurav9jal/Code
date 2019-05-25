### Move all zeroes to end of array

def moveToEnd(list):
    if(len(list) == 0):
       return 
    else:
      index = 0
      for ite in range(0,len(list)):
          if(list[ite] != 0):
              list[index] = list[ite]
              index+=1
      while(index < len(list)):
         list[index] = 0
         index+=1

    return list  
print(moveToEnd([1,2,0,4,3,0,5,0]))


