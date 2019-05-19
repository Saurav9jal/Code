###Unbounded Knapsack (Repetition of items allowed)

def unboundedKnapsack(list1,list2,W):
    dp = [0 for index in range(0,W+1)]
    for index in range(0,W+1):
        for j in range(0,len(list2)):
           if(list2[j] <= index):
                dp[index] = max(dp[index],dp[index - list2[j]] + list1[j])
    return dp

list1 = [10,30,20]
list2 = [5,10,15]
W =100
print(unboundedKnapsack(list1,list2,W))







