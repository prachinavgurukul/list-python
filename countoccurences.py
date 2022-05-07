# char_list=["a","n","t","a","a","t","n","n","a","x","u","g","a","x","a"]
# i=0
# a=[]
# count=0
# while i<len(char_list):
#     if char_list[i] not in a:
#         a.append(char_list[i])
    
#     i=i+1
# print(a)


char_list=["a","n","t","a","a","t","n","n","a","x","u","g","a","x","a"]
i=0
count=0
a=[]
while i<len(char_list):
    if char_list[i] not in a:
        a.append(char_list[i])
        count=count+1
    i=i+1
print(a,count)