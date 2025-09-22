from random import randint

target=randint(1,10)

attemt=0

while True:

    num=int(input("enter number"))
    attemt+=1


    if target==num:

        print(attemt,"times")

        print("congrats")

        break


target=2

while True:

    num=int(input("enter number :"))

    if num==target:

        print("congrats")

        break