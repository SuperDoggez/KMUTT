def multi(a,f):
    if f <= 12 :
        print(a ,"X" , f , "=" , a*f)
        return multi(a,f+1)
num = int(input("Enter a number : "))
print("Multiplication Table of {} is : ".format(num))
f=1
multi(num,f)