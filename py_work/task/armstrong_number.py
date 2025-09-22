number = int(input("enter number"))

sum = 0

c_number= len(str(number))

org=number

# print(c_number)

while number !=0:

    digit=number%10

    expo =digit**c_number

    sum=expo+sum

    number=number//10

print(sum)


if org==sum:
    print("Armstrong number")

else:

    print("NOt armstrong number")   



