##### Longest Consecutive Subsequence


def findLongestC(list): 
    if(len(list) == 0):
        return 
    max_num =-10000
    current_num = 0
    dict ={}
    for num in list:
        dict[num] = 0
    for num in list:
        temp_num = num
        current_num = 0
        while(temp_num  in dict.keys()):
             current_num +=1
             temp_num -=1
        if(max_num < current_num):
            max_num = current_num
    print(max_num)



list = [1, 9, 3, 10, 4, 20, 2]
findLongestC(list)









