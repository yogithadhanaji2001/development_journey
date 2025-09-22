number=int(input("enter number :"))
org=number

reversed=0

while number!=0:

    digit=number%10

    reversed=reversed*10+digit

    number=number//10

print("palandrome number " if reversed==org else "not palandrome" )
