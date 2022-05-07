a=[4,6,3,5,11,7,2,1]
i=0
b=0
while i<len(a):
    if a[i]>b:
        b=a[i]
    i=i+1
i=0
c=0
while i<len(a):
    if a[i]>c and a[i]!=b:
        c=a[i]
    i=i+1

i=0
d=0
while i<len(a):
    if a[i]>d and a[i]!=c and a[i]!=b:
        d=a[i]
    i=i+1
print("first max no is",b)
print("second max no is",c)
print("third max no is",d)