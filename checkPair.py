### Given an array A[] and a number x, check for pair in A[] with sum as x


def findPair(list,sum):
    if(len(list) == 0):
        return 
    dict = {}
    for index in list:
       if((sum - index) in dict.keys()):
            print("pairs are {} {}".format(index,sum-index))
       else:
            dict[index] = 0

list = [1, 4, 45, 6, 10, -8]
findPair(list,16)

