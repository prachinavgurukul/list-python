input_list=[1,2,2,5,8,4,4,8]
a=[]
i=0
while i<len(input_list):
    if input_list[i] not in a:
        a.append(input_list[i])
    i=i+1
print(a)