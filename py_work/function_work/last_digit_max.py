# create a function last_digit_max with parameter num1,num2

# function should return num1 if last digit of num1 >num2 else return num2


def last_digit_max(num1,num2):

    return num1 if num1%10 > num2%10 else num2

print(last_digit_max(123,119))



    

