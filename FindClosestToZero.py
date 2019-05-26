### Two elements whose sum is closest to zero



def findClosest(list1):
    if(len(list1) == 0):
       return 
    max_sum = 10000
    list1.sort()
    i = 0
    j = len(list1) -1
    while(i != j):
      current_sum = (list1[i]+list1[j])
      if(abs(current_sum) < max_sum) :
          max_sum = abs(current_sum)
      if(current_sum > 0):
          j-=1
      else:
          i += 1
    print(max_sum)

list = [1, 60, -10, 70, -80, 85]
findClosest(list)
      



