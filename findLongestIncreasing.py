### Longest Increasing Subsequence | DP-3

def findLongestIncreasing(list):
    if(len(list) == 0):
        return 
    list1 = [1]*len(list)
    for index in range(1,len(list)):
       for index1 in range(0,index):
          if(list[index1] < list[index]):
              list1[index] = max(list1[index1]+1,list1[index])
    print(list1)


list = [3, 10, 2, 1, 20]
findLongestIncreasing(list)










