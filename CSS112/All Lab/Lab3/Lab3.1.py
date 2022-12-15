def Checkname(name) :
    name = name.capitalize()
    if name in name_list :
        print("Hello, {}. Good morning my friend!" .format(name))
    else :
        print("Who are you? /n Nice to meet ypu anyway ... {} :)." .format(name))

name = str(input("What is your name? : "))
name_list = ["Jeff","Jack","Jim"]
Checkname(name)

btrrat = ()

