def zipcodes(kod1,kod2):

    codes=[]
    start=''
    end=''

    for i in kod1:
        if i.isdigit():
            start+=i
    start=int(start)

    for i in kod2:
        if i.isdigit():
            end+=i
    end=int(end)

    if end<start:
        tmp=end
        end=start
        start=tmp

    for i in range(start+1,end):
        i=str(i)
        i=i[:2]+'-'+i[2:]
        codes.append(i)

    return(codes)
