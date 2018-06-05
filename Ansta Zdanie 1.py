def zipcodes(kod1,kod2):
    codes=[]
    start=''
    end=''
    tmp=0
    for i in kod1:
        if i.isdigit():
            start+=i
    start=int(start)
    print(start)
    for i in kod2:
        if i.isdigit():
            end+=i
    end=int(end)
    print(end)
    if end<start:
        tmp=end
        end=start
        start=tmp
    elif end==start:
        print('Kody sa takie same')
    for i in range(start+1,end):
        i=str(i)
        i=i[:2]+'-'+i[2:]
        codes.append(i)
    print(codes)
zipcodes('10-20','9-9')