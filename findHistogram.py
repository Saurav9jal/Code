#### Maximum Rectangular Area in Histogram


def findHistoram(list):
     if(len(list) == 0):
         return 
     stack = []
     max_area = 0
     stack.append(list[0])
     for index in range(1,len(list)):
         if(list[index] >= list[stack[-1]]):
              stack.append(index)
         else:
              while(list[stack[-1]] > list[index]):
                  num = stack.pop()
                  if(len(stack) != 0):
                    area = list[num] * (index - 1 - stack[-1])
                    if(max_area < area):
                        max_area = area
                  else:
                        area = list[num]*index
                        if(max_area < area):
                            max_area = area
                        if(len(stack) == 0):
                            break     
              stack.append(index)                     
     while(len(stack)!=0):
         num = stack.pop()
         if(len(stack) != 0):
           area = list[num] * (index - 1 - stack[-1])
           if(max_area < area):
                max_area = area 
         else:
            area = list[num]*len(list)
            if(max_area < area):
                 max_area = area  
     print(max_area)

findHistoram([6, 2, 5, 4, 5, 1, 6])


