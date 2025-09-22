def palindrome(num):

    
    number=0

    while num !=0:

        digit=num%10

        number= number*10+digit

        num=num//10

    return number

print(palindrome(121))





def palindrome(num):

    
    reversed=0

    while num >0:
        digit= num%10
        reversed=reversed*10+digit
        num=num//10
    return reversed

print(palindrome(122))    



    


