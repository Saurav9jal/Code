#### Given an array A[] and a number x, check for pair in A[] with sum as x


def checkSumInArray(array,sum):
    if(len(array) == 0):
        return 
    else:
        dict = {}
        for num in array:
            if((sum - num) in dict.keys()):
                print("numbers are {} {}".format(num,sum-num))
            else:
                dict[num] = 0


array = [1, 4, 45, 6, 10, 8]
sum = 16
checkSumInArray(array,sum)




    









