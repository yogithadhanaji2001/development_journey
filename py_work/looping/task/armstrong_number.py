num= int(input("enter number"))

org=num

sum=0

c_num=len(str(num))

for i in range (num):

    digit = num %10

    expo=digit**c_num

    sum=sum+expo

    num= num//10

print("armstrong number " if org==sum else "not armstrong number")