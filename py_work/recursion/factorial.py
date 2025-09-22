n=5
fact=1

# for i in range (1,n+1):

#     fact=fact*i

# print(fact)


def factorial(n):

    if n==0:

        return 1
    
    return n*factorial(n-1)

print(factorial(5))




def sum(n):

    if n==0:

        return 0
    
    return n+sum(n-1)


print(sum(5))



def digit_sum(n):

    if n==0:

        return 0
    
    return n%10+digit_sum(n//10)

print(digit_sum(345))