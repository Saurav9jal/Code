### Next Greater Element

def findNextGreater(list):
    if(len(list) == 0):
         return 
    else:
        FirstIndex = True
        while(len(list) != 0):
          if(FirstIndex == True):
               num = list.pop()
               print("next greater element is {}".format(-1))
               FirstIndex = False
          else:
              if(list[-1] < num):
                 print("next greater element is {}".format(num))
                 temp_num = list.pop()
                 if(len(list)!= 0 and temp_num > list[-1]):
                     num = temp_num
              else:
                 num = list.pop()
                 print("next greater elelemnt is {}".format(-1))



list = [11,13,21,3]

findNextGreater(list)
