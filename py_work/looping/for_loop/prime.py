num= int(input("enter number"))

is_prime=True

for i in range (2,num):

    if num % 2== 0:

        is_prime=False

        break


print("prime number" if is_prime== True else "not prime")  