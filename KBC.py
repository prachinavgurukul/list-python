# question_list=[
#    ["How many continents are there?"],
#     ["What is the capital of india?"],
#     ["NG mei kaun se course padhaya jata hai?"],
#     ["B"]
#  ]
# options_list=[
#     ["four","nine","seven","eight"],
#     ["chandigarh","bhopal","chennai","delhi"],
#     ["software engineer","counselling","tourism","agriculture"]
#    ]
# life_line50_50=[["1)four","3)seven"],
#                 ["2)bhopal","4)delhi"],
#                 ["1)software engineer","4)agriculture"],
#                 ]
# solution=[3,4,1]
# i=0
# a=0
# b=10000
# while i<len(question_list):
#     print(question_list[i])
#     c=0
#     while c<len(options_list[i]):
#         k=(options_list[i][c])
#         print(c+1,k)
#         c=c+1
#     if a==0:
#         d=input("do you want life line?")
#         if d=="yes":
#                 a+=1
#                 print(life_line50_50[i])
#                 b+=10000
#     ans=int(input("enter the answer:"))
#     if solution[i]==ans:
#         print("congratulation!You are winner with price🥳",b)
#         b+=20000
#     else:
#         print("Koi nhi beta next time try krna😊")
#     i+=1




a=int(input("enter the no:"))
b=a%1000//100
if b==2:
    print("yes")
else:
    print("no")

