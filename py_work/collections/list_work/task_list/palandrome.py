
# numbers =[11,12,13,33,131,343,12321,1234]

# display palindromic numbers from list


def palindrome(number):

    org=number

    
    reversed=0

    while number >0:
        digit= number%10
        reversed=reversed*10+digit
        number=number//10

    return reversed == org

# print(palindrome(122)) 


numbers =[11,12,13,33,131,343,12321,1234]


for num in numbers:

    if palindrome(num):
        print(num)
  

