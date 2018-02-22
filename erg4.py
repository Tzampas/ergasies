x=int(input("dwse fysiko arithmo mikrotero toy 1000000 \n"))
tel=""
a=0
b=x
c=0
k=0
lat=("I","V","X","L","C","D","M","V","X")
def n(z,d,i):
    a=""
    if (z==9):
        a=d[i]+d[i+2]
    elif (z>3):
        a=d[i+1]+d[i]*(10-z)
    elif (z<=3):
        a=d[i]*z
    return a
if (x//1000000==1):
    print("_ \n","M")
else:
    if (x//100000>0):
        tel=n(x//100000,lat,4)
        a=len(tel)
		b=x%100000
    if (b//10000>0):
        tel+=n(b//10000,lat,2)
        a+=len(n(b//10000,lat,2))
        b=b%100000
    if(b//1000>0):
        tel+=n(b//1000,lat,6)
        if(b>=9000):
            c=1
            k+=1
        b=b%1000
    if(b//100>0):
        tel+=n(b//100,lat,4)
        b=b%100
		 if(b//10):
        tel+=n(b//10,lat,2)
        b=b%10
    if(b//1):
        tel+=n(b,lat,0)
    print(""*a," "*c,""*k,"\n",tel)