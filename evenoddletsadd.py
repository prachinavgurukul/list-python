elements=[23,14,56,12,19,9,15,25,31,42,43]
o=[]
e=[]
i=0
esum=0
osum=0
while i<len(elements):
    if elements[i]%2==0:                                                                                                                                                                                              
        e.append(elements[i])
        esum=esum+elements[i]
    else:
        o.append(elements[i])
        osum=osum+elements[i]
    i=i+1
print("even list:",e)
print("odd list:",o)
print(esum)
print(osum)
