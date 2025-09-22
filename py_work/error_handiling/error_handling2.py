
num1=int(input("enter number"))

num2=int(input("enter number"))

try:
    res=num1/num2
    print(res)

except Exception as e:

    num2=int(input("enter number"))

    res=num1/num2

    print(res)
    
finally:    
    
    print("send text message to user phone")

    print("sent email confirmation")