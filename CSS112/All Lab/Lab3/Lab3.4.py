def listfn(numelement):
    for i in range(numelement) :
        num = int(input())
        listofnum.append(num)

numelement = int(input("Enter number of elements : "))
listofnum = []
listfn(numelement)
print("The entered list is ",listofnum)
print("The maximum number entered is ",max(listofnum))
print("The minimum number entered is ",min(listofnum))