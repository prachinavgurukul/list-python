a=[1,2,3,4,5,6]
i=0
sum=0
product=1
while i<len(a):
    if a[i]%2==0:
        sum=sum+a[i]
    else:
        product=product*a[i]
    i=i+1
print("sum of even no is",sum)
print("product of odd no is",product)