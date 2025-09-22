number =int(input("enter number"))

c_num=len(str(number))
sum=0
org=number

while number !=0:

    digit=number%10

    

    expo=digit**c_num

    sum=sum+expo

    number=number//10


print("armstrong number " if org==sum else "not armstrong")  

