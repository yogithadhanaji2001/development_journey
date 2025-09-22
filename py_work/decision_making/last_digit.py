# read a number

# write a program that display last of number is odd or even

num = int(input("enter number"))

last_digit = num % 10

if last_digit % 2 ==0:
    print("even")

else:
    print("odd")
