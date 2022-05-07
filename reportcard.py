marks=[
    [78,76,94,86,88],
[91,71,98,65,76],
[95,45,78,52,49]
]
i=0
sum=0
while i<len(marks):
    j=0
    while j<len(marks[i]):
        sum=sum+marks[i][j]
        j+=1
    avgsum=sum//len(marks[i])
    print("Total sum:",sum)
    print("Average of sum:",avgsum)
    sum-=sum
    i+=1
    