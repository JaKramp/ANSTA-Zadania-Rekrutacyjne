def missing(numbers,length):
    elements=set()
    mising=[]
    for i in range(len(numbers)):
        elements.add(numbers[i])
    print(elements)
    for i in range(1,length+1):
        if i not in elements:
            mising.append(i)
    print (mising)
missing([2,3,7,4,9],10)
