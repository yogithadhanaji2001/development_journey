# age= int(input("enter age"))

# if age<18:

#     raise Exception("invalid age")


# print("approve")


def divide (num1,num2):

    if num2==0:

        raise Exception ("num2 not be zero")
    
    else:
        return num1/num2
    

print(divide(10,2))    