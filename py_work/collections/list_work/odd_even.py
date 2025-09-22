arr=[1,10,11,12,34,35]

# create a new array odd arr and even arr


odd=[]
even=[]

for num in arr:

    if num %2 ==0:

        even.append(num)

    else:
        odd.append(num)    

print(odd)
print(even)        