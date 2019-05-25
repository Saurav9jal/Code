## Sort an array of 0s, 1s and 2s

def sortArray(list):
    count0 = 0
    count1 = 0
    count2 = 0
    for arr in list:
        if(arr == 0):
          count0 +=1
        if(arr == 1):
          count1 += 1
        if(arr == 2):
          count2 += 1
    for index in range(0,len(list)):
        if(count0 != 0):
          list[index] = 0
          count0 -=1
        elif(count1 != 0):
          list[index] = 1
          count1 -=1
        else:
          list[index] = 2
          
    for arr in list :
       print("array element are {}".format(arr))


sortArray([0,1,2,0,1,2])









