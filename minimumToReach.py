### Minimum number of jumps to reach end

def minimumToR(list):
    if(len(list) == 0):
       return 
    list1 = [1000]*len(list)
    list1[0] = 0
    for index in range(1,len(list)): 
        for index1 in range(0,index):
            if((list[index1] + index1) >= index):
               list1[index] = min(list1[index1]+1,list1[index])



list =[1, 3, 6, 3, 2,3, 6, 8, 9, 5]
minimumToR(list)        











