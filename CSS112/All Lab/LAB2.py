#1
Temp = float(input("Please enter the temperature in Celsius : ")); print("The {:.1f} Celcius = {:.1f} Farenhite".format(Temp,(9*Temp/5)+32))

#2
Num2 = int(input("Enter number "))
Sum2 = 0
for i in range(1,Num2+1) :
    Sum2 = i+Sum2
print("Summation of numbers from 1 to {} is : {}".format(Num2,Sum2))

#3
Num3 = int(input("Enter a number to make a multiplication table : "))   
for i in range(1,13) :
    print(Num3, "X", i ,"=", Num3*i)

#4
Score = int(input("Please enter your score : "))
Grade = 0
if Score>=80 :
    Grade = "A"
elif 79>=Score>=75 :
    Grade = "B+"
elif 74>=Score>=70 :
    Grade = "B"
elif 69>=Score>=65 :
    Grade = "C+"
elif 64>=Score>=60 :
    Grade = "C"
elif 59>=Score>=55 :
    Grade = "D+"
elif 54>=Score>=50 :
    Grade = "D"
else :
    Grade = "F"
print("You got" ,Grade)

#5
Start = int(input("Please enter a starting number : "))
End = int(input("Please enter an ending number : "))
print("Prime numbers between {} and {} are :".format(Start,End))
for i in range(Start,End+1):
    if i > 1 :
        for o in range(2,i):
            if(i % o == 0):
                break
        else:
            print(i)

    
    