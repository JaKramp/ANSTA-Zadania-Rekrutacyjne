def missingelements(numbers,length):
    elements=set()
    missing=[]
    for i in range(len(numbers)):
        elements.add(numbers[i])
    print(elements)
    for i in range(1,length+1):
        if i not in elements:
            missing.append(i)
    return (missing)

