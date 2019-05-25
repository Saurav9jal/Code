#### Reverse words in a given string

def reverseString(str):
    if(len(str) == 0):
        return 
    newString = ""
    for index in reversed(range(0,len(str))):
        newString =   newString + str[index]
    print(newString)

str = "i love you" 
reverseString(str)
   
       

