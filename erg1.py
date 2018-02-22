import random
a=0
p=[]
f=0
for i in range(1000):
    b=[]
    c=range(1,81)
    s=0
    for x in range(100):
        p[x]=random.sample(range(1,81),5)
        i=0
        while (i==0):
            s+=1
            random.suffle(c)
            b[s-1]=c.pop(80-step)
            print(b[s-1])
            for y in range(100):
                if (p[y] in b):
                    i+=1
                    print("bingo!")
    f+=s
print(s/10000)