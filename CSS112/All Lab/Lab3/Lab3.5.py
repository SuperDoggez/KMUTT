def area_tri():
    base = int(input("Please enter the base length : "))
    height = int(input("Please enter the height : "))
    area = 0.5 * base * height
    return area,base,height

def area_cubic():
    width = int(input("Please enter the base width : "))
    lenght = int(input("Please enter the lenght : "))
    height = int(input("Please enter the height : "))
    area = width * lenght * height
    return area,width,lenght,height

def area_cone():
    base = int(input("Please enter the base diameter : "))
    height = int(input("Please enter the height : "))
    area = (1/3)*(22/7)*((base/2)**2)*height
    return area,base,height


print("Please enter a choice for your selection : \n Enter 1 if you want to calculate the area of a triangle. \nEnter 2 if you want to calculate the volumn of a cubic. \n Enter 3 if you want to calculate the volumn of a cone.")
choice = int(input("Enter your choice here : "))
if choice == 1:
    area = area_tri()
    print("The area of triangle with base = {} and height = {} is {:.1f}".format(area[1],area[2],area[0]))
elif choice == 2:
    area = area_cubic()
    print("The cubic volumn of width = {} lenght = {} and height = {} is {}".format(area[1],area[2],area[3],area[0]))
elif choice == 3:
    area = area_cone()
    print("The conical volumn of cone with diameter = {:.1f} and height = {:.1f} is {}".format(area[1],area[2],area[0]))
else :
    print("Invalid Choice")


