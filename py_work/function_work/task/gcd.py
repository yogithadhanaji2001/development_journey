def gcd(num1,num2):

    gcd=1
    limit=min(num1,num2)

    for i in range(1,limit+1):

        if num1%i==0 and num2%i==0:

            gcd=i

    return gcd    


print(gcd(3,6))

