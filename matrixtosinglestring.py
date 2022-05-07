# list=[["g","f","g"],["i","s"],["b","e","s","t"]]
# i=0
# a=[]
# while i<len(list):
#     j=0
#     while j<len(list[i]):
#         b=(list[i][j])
#         a.append(b)
#         c="".join(a)
#         j=j+1
#     i=i+1
# print(c)

# b=int(input("enter the no"))
# a=[1,4,7,8,9,10,11]
# i=0
# count=0
# while i<len(a):
#     if a[i]>b:
#         count+=a[i]
#     i=i+1
# print(count)

a=int(input("enter the name:"))
i=0
c=[]
while i<a:
    b={}
    name=input("enter the name:")
    age=int(input("enter the age:"))
    sur=input("enter teh sum:")
    b.update({"name":name,"age":age,"sur":sur})
    c.append(b)
    i+=1
print(c)


   

    


    
