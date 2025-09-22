# create a function max odd number with one parameter(num)

# that will return  largest odd number from number


def max_odd_number(num):

    while num !=0:

        last_digit= num%10

        if last_digit%2 !=0:

            return(num)

            break

        num = num//10

print(max_odd_number(12345678))




