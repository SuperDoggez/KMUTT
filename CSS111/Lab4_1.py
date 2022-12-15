def myreplace(sentence,old,new):
    res=''; i=0; flags=0
    while i < len(sentence):
        if sentence[i:i+len(old)] == old:
            res+=new
            flags+=1 
            i+=len(old)
        res+=sentence[i]
        i+=1
    ans=res+'\n'+str(flags)
    return ans
sentence = input()
old = input()
new = input()
print(myreplace(sentence,old,new))