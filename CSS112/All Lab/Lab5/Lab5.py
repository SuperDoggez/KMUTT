#1
try:
    file1 = open("/Users/chanchanon/Documents/Work/CSS112/Lab5/myFile.txt","r")
    print(file1.read())
    file1.close()
except:
    print("Unable to open file myFile.txt")
else:
    print("Successfully print content in myFile.txt")

#2
file1 = open("/Users/chanchanon/Documents/Work/CSS112/Lab5/myFile.txt","r")
data = file1.read()
striptext = data.strip()
lenfile1 = len(striptext)
print("Total leter are ",lenfile1)
file1.close()

#3
file1 = open("/Users/chanchanon/Documents/Work/CSS112/Lab5/myFile.txt","r")
data = file1.read()
splitfile = data.split()
print("Total word are ",len(splitfile))
file1.close()

#4
def temp_cal(start,end):
    if start <= end :
        Faren = (((9*start))/5)+32
        file1.write("{} Celcius = {:.1f} Farenheit. \n".format(start,Faren)) 
        return temp_cal(start+1,end)
    else :
        return
file1 = open("/Users/chanchanon/Documents/Work/CSS112/Lab5/multiply.txt","w")
start = int(input("Enter a beginning Celcius value : "))
end = int(input("Enter an ending Celcius value : "))
temp_cal(start,end)
file1.close()


