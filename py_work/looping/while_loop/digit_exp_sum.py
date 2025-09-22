num = int(input("enter number"))

count =len(str(num))

sum=0
exp=1

while num !=0:

    digit = num % 10


    exp = digit**count


    sum = sum+exp

    num = num//10

print(sum)    






    

   

