def checknum(num):
    value=0
    res='True'
    for i in range(len(num)):
        if i > 0 and value==0:
            if int(num[i]) > int(num[i-1]):
                value=1
                continue
            elif int(num[i]) < int(num[i-1]):
                value=2 
                continue   
        if value == 1 and int(num[i]) > int(num[i-1]):
            res="False"
            return res
        elif value == 1 and int(num[i]) < int(num[i-1]):
            value=0
        if value == 2 and int(num[i]) < int(num[i-1]):
            res="False"
            return res
        elif value == 2 and int(num[i]) > int(num[i-1]):
            value=0  
    return res
    

num=int(input())
res=checknum(str(num))
print(res)
                       
        
                
            
