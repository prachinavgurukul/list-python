kitna_paisa_hai=[3000,600000,324990909,90990900,30000,5600000,690909090,31010101,532010,510,4100]
crorpati=[]
lakhpati=[]
dilwale=[]
i=0
while i<len(kitna_paisa_hai):
    if kitna_paisa_hai[i]>=10000000:
        crorpati.append(kitna_paisa_hai[i])
    elif kitna_paisa_hai[i]>=100000 and kitna_paisa_hai[i]<10000000:
        lakhpati.append(kitna_paisa_hai[i])
    else:
        dilwale.append(kitna_paisa_hai[i])
    i=i+1
print(crorpati)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
print(lakhpati)
print(dilwale)
