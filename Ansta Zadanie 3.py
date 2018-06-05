from decimal import *
def listgenerator(start,end):
    list=[]
    startingpoint=int(2*start)
    limit=int(2*end)

    for i in range(startingpoint,limit+1):
        list.append(Decimal(i/2))
    print(list)
    print(type(list[2]))
listgenerator(2,5.5)