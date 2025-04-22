def fibonnaciseries():
    num = int(input("Enter a number"))
    count=0
    a,b=0,1
    if num < 0:
        print("Enter a positive number:")
    elif num ==0:
        print("Enter a number greater than 0")
    else:
        print("fibonnaci series is:")
        while count < num:
            print(a)
            a,b = b,a+b
            count+=1
fibonnaciseries()