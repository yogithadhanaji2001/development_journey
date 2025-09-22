# read two number n1 and n2 display largest number amount two numbers


n1=int(input("enter number :"))

n2= int(input("enter number :"))


if n1>n2:
    print(n1)

else:
    print(n2)    



# read three numbers n1,n2,n3 display largest amount three

n1= int(input("enter number :"))
n2= int(input("enter number :"))
n3= int(input("enter number :"))


if n1>n2 and n1>n3:
    print(n1)

elif n2>n1 and n2>n3:
    print(n2)

elif n3>n2 and n3>n1:
    print(n3)        
 