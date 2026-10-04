n=int(input("Enter a numder: "))
digits=len(str(n))
r=0
t=n
while t>0:
    d=t%10
    r=r+d**digits
    t=t//10

if r==n:
    print(n,"is a armstrong number")
else:print(n,"is not a armstrong number")