#Check Status Assignment:
def checkstatus(a,b,flag):
    if flag:
        return a<0 and b<0
    else:
        return a<0<=b or b<0<=a
print("Status is:", checkstatus(-1,0,True))  
print("Status is:", checkstatus(99,89,True))  
print("Status is:", checkstatus(-45,-78,True))  