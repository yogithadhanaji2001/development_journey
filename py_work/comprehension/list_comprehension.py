
arr=[1,2,3,4,5,6,7]

square=[]

for i in arr:

    square.append(i**2)


print(square)


# eassy way for creating list,set,,dictonary,from an itrable

# syntax
# [expression itration condition(optional*)]

square=[num**2 for num in arr ]
print(square)



fruits=["apple","banana","carrot","drumstick"]

new=[item.upper() for item in fruits]
print(new)


even=[num for num in arr if num%2==0]

print(even)

odd=[num for num in arr if num %2 !=0]
print(odd)


