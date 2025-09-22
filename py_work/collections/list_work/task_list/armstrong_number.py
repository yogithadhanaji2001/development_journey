
num=int(input("enter number"))

c_number=len(str(num))

org=num

sum=0

while num !=0:

    digit=num%10

    expo=digit**c_number

    sum=sum+expo

    num=num//10

print("armstrong number" if org==sum else "not armstrong")    


def is_armstrong(number) :

    c_number=len(str(number))

    org=number
    sum=0

    while (number!=0):

        digit=number%10
        expo=digit**c_number
        sum=sum+expo
        number=number//10

    return sum==org

print(is_armstrong(153))         

numbers=[151,152,153,1634,8891,345,678]


for num in numbers:

    if is_armstrong(num):

        print(num)