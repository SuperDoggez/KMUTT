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