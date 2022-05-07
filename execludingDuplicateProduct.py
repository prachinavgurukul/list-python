list=[6,1,3,5,6,3,1]
i=0
b=[]
while i<len(list):
    if list[i] not in b:
        b.append(list[i])
    i=i+1
print(b)
j=0
p=1
while j<len(b):
    p=p*b[j]
    j=j+1
print(p)
    
    