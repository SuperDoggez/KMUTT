def getfullname(name,surname):
    def getname() :
        return name + " " + surname
    print("Hi!,", getname(), "!")


name = input("What is your name? :")
surname = input("What is your last name?: ")
getfullname(name,surname)