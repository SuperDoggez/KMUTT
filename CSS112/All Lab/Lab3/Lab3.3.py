def prime_check():
    Value_prime = False
    if Num > 1 :
        for i in range(2,Num):
            if(Num % i == 0):
                break
        else:
            Value_prime = True
    return Value_prime


Num = int(input("Enter a number to test : "))
Value = prime_check()
if Value == True :
    print("This is a prime number")
else :
    print("This is not a prime number")
