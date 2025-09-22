# sum of square of first n natural number
# 1*2+2*2+3*2+....


n=int(input("enter number :"))
sum=0
square=1

for i in range (1,n+1):

    square=i**2

    sum=sum+square


    print(sum)    