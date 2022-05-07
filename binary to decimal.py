                                                                                                                                                                    

binary=[1, 0, 0, 1, 1, 0, 1, 1]
i=0
decimal=0
while i<len(binary):
    a=binary[-i -1]                        
    decimal=decimal+a*(2**i)
    i+=1
print(decimal)  
               
