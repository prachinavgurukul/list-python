# n=[50,40,23,70,56,12,5,10,7]
# a=n[0]
# i=0
# while i<len(n):
#     if n[i]>a:
#         a=n[i]
#     i=i+2
# print(a)
# a=0
# i=0
# while i<len(n):
#     if n[i]>a:
#         a=n[i]
#     i=i+1
# j=0
# b=0
# while j<len(n):
#     if n[j]>b and n[j]!=a:
#         b=n[j]
#     j=j+1
# print(b)
# t=int(input("w"))
# for i in t:
#     str=input()
#     print ("True")


# a=  1,2,3,
# 2,3,4,
# 5,6,7
# arr=[]
# left=right=0
# for i in a:
#     left+=arr[i][i]
#     right+=arr[i][n-1-i]
# print(left)

# a=[5,5,4,4,3,3,2,2,1,1,0,0]
# print(sorted(set(a)))

i=5
while i>=1:
    j=1
    while j<=i:
        print(i,end="")
        j=j+1
    print()
    i=i-1

