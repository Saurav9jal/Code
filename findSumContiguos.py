####   Largest Sum Contiguous Subarray

def findSumContiguos(list):
    if(len(list) == 0):
        return 0
    list1 = [0]*len(list)
    for index in range(0,len(list)):
          if(index == 0):
            list1[index] = list[index]
          else:
            if((list1[index-1] + list[index]) > list[index]):
                 list1[index] = list1[index-1] + list[index]
            else:
                 list1[index] = list[index]
    print(list1)


list = [-2, -3, 4, -1, -2, 1, 5, -3]
findSumContiguos(list)     
      












