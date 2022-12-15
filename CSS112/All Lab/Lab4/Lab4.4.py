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
