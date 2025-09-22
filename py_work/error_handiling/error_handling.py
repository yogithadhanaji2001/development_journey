"""
Error handling

1) syntax error
2) run error

keywords:

try
except
finally
raise
assert

blocks => try, except,finally

try:
    doubtful code

except:
    handling code   


finally:
    clean up process


raise key custom error throw

assert debugging

"""


num1=int(input("enter number"))

num2=int(input("enter number"))

try:
    res=num1/num2
    print(res)

except:
    print("error occur")


print("send text message to user phone")

print("sent email confirmation")

