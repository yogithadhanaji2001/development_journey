num = int(input("enter number"))
num1 = int(input("enter number"))

limit = min(num,num1)

gcd=1

for i in range (1,limit+1):

    if num %i ==0 and num1 %i==0:

        gcd=i
print(gcd)    