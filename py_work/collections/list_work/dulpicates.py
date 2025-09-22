arr1=[10,11,20,17,18,10]
arr2=[20,10,12,17]

arr=[]

for num in arr1 :

    if arr2.count(num)>0:

        arr.append(num)

print(arr)        



for num in arr1:

    if num in arr2:

        print(num)