#1
def getfullname(name,surname):
    def getname() :
        return name + " " + surname
    print("Hi!,", getname(), "!")


name = input("What is your name? :")
surname = input("What is your last name?: ")
getfullname(name,surname)

#2
def temp_cal(start,end):
    if start <= end :
        Faren = (((9*start))/5)+32
        print("{} Celcius = {:.1f} Farenheit.".format(start,Faren)) 
        return temp_cal(start+1,end)
    else :
        return

start = int(input("Enter a beginning Celcius value : "))
end = int(input("Enter an ending Celcius value : "))
temp_cal(start,end)

#3
def multi(a,f):
    if f <= 12 :
        print(a ,"X" , f , "=" , a*f)
        return multi(a,f+1)
num = int(input("Enter a number : "))
print("Multiplication Table of {} is : ".format(num))
f=1
multi(num,f)

#4

def ticket_cal(name,age):
    price = 15.0
    def condition():
        if (name in members) and age < 15:
            print("Ticket price for {} is: $".format(name),price*(25/100))
        elif (name in members) and age >= 15:
            print("Ticket price for {} is: $".format(name),price*(50/100))
        elif age < 15:
            print("Ticket price for {} is: $".format(name),price*(50/100))
        else:
            print("Ticket price for {} is: $".format(name),price)
    condition()

members = ["Tony", "Peter", "Mark", "Kim", "James", "Kenny"]
name = input("Please enter your name: ").capitalize()
age = int(input("Please enter your age: "))
ticket_cal(name,age)
