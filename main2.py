def r(p):
    roman={'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
    res=0
    for i in range(0,len(p)-1):
        if roman[p[i]]<roman[p[i+1]]:
            res-=roman[p[i]]
        else:
            res+=roman[p[i]]
    return res+roman[p[-1]]
roman=input("Enter a roman number: ")
print("The integer of",roman,"is",r(roman))