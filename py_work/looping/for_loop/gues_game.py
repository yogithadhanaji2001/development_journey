# tagert = 2

# while True:

#     num= int(input("enter number"))

#     if num ==tagert:

#         print("congrats")

#         break


from random import randint

target = randint(1,10)

attempt=0

while True:

    num = int(input("enter number"))

    attempt=attempt+1


    if num ==target:

        print(attempt, "times")

        print("congrats")

        break


    