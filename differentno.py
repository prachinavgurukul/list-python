list1=[1,2,3,4,5,6]
list2=[2,3,1,0,6,7]
c=[]
i=0
while i<len(list1):
    b=list1[i]
    if b not in list2:
       c.append(b)
    i=i+1
print(c) 






