elements=[23,14,56,12,19,9,15,25,31,42,43]
o=[]
e=[]
i=0
count=0
count1=0
count2=0
esum=0
osum=0
while i<len(elements):
    count=count+1
    if elements[i]%2==0:
        e.append(elements[i])
        esum=esum+elements[i]
        esumavg=esum/4
        count1=count1+1
    else:
        o.append(elements[i])
        osum=osum+elements[i]
        osumavg=osum/7
        count2=count2+1
    i+=1
print("list of even:",e)
print("list of odd:",o)
print("count of elements:",count)
print("sum of even no:",esum)
print("sum ofodd no:",osum)
print("average of even no:",esumavg)
print("average of odd no:",osumavg)
print("count of even list:",count1)
print("count of odd list:",count2)
    


