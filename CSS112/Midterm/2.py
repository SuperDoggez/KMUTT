def centoinch():
    inch = centimeter_input / 2.54
    return inch

def kgtopond():
    pond = weight_input * 2.2
    return pond

def CtoF() :
    temp = ((9*temp_input)/5)+32
    return temp

def littoUS():
    Us = Litre_input /3.785
    return Us
print("Select an operation. \n\n 1.Convert Centimeter into Inch \n 2.Convert Kilogram into pound \n 3.Convert Celcius into Farenheitn \n 4.Convert Litre into US Gallon")
n=1
while (n==1):
    menu_input = int(input("Enter choice (1/2/3/4) : "))
    if menu_input == 1 :
        centimeter_input = float(input("Enter dimension in Centimeter : "))
        centoinch()
        inch = centoinch()
        print("The {} Centimeter(s) equal to {:.2f} inch(es).".format(centimeter_input,inch))
        con = input("Let's do next calculation? (y/n) : ")
        if con != "y" :
            n=0
        
 
    elif  menu_input == 2 :
        weight_input= float(input("Enter weight in Kilogram : "))
        kgtopond()
        pond = kgtopond()
        print("The {} Kilogram(s) equal to {:.2f} Pound(s)).".format(weight_input,pond))
        con = input("Let's do next calculation? (y/n) : ")
        if con != "y" :
            n=0


    elif menu_input == 3 :
        temp_input = float(input("Enter temperature in Celcius : "))
        CtoF()
        temp = CtoF()
        print("The {} Celcius(es) equal to {:.2f} Farenheit(s).".format(temp_input,temp))
        con = input("Let's do next calculation? (y/n) : ")
        if con != "y" :
            n=0

    elif menu_input == 4 :
        Litre_input = float(input("Enter volume in Litre : "))
        littoUS()
        Us = littoUS()
        print("The {} Litre(s) equal to {:.2f} US Gallon(s).".format(Litre_input,Us))
        con = input("Let's do next calculation? (y/n) : ")
        if con != "y" :
            n=0

    else :
        print("Invalid Input")
        continue
    

        
