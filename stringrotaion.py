def stringrotation(str1,str2):
    if len(str1)!=len(str2):
        return 0
    else:
        temp=str1+str1
        if (temp.count(str2)>0):
            return 1
        else:
            return 0
str1="amarths"
str2="samarth"
if(stringrotation(str1,str2)):
    print("yes")
else:
    print("no")