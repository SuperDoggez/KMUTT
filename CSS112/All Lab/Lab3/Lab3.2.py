def Cal_Salary():
    if hour<=40 :
        Salary = hour*rate
        print(Salary)
    elif hour>=40 :
        Salary = (40*rate) + ((hour-40)*(rate*1.5))
        print(Salary)
            

hour = float(input("How many hours did you work last week : "))
rate = float(input("What is your pay rate per hour (between 10-25) : "))
Cal_Salary()
