n=[1,2,3,4,5]
sum=0
i=0
b=[]
a=[]
while i<len(n):
    if n[i]%2==0:
      sum=sum+n[i]
      b.append(sum)
    else:
        sum=sum+n[i]
        a.append(sum)
    i=i+1
print(a)
print(b)