from decimal import *
def listgenerator(start,end):
    list=[]
    begin=int(2*start)
    finish=int(2*end)+1

    for i in range(begin,finish):
        list.append(Decimal(i/2))
    return(list)