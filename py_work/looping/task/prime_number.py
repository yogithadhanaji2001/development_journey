
num = int(input("enter number :"))

prime=True

for i in range (2,num):

    if num % 2 ==0:

        prime=False

        break

print("prime number" if prime== True else "not prime")  

